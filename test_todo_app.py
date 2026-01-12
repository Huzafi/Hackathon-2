"""Test script for Phase I Console Todo App.

This script performs automated testing of the todo application functionality.
"""

import sys
import os
import io

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from services.todo_service import TodoService
from models.todo import Todo


def test_add_todo():
    """Test adding todos."""
    print("Testing: Add Todo")
    service = TodoService()

    # Test valid add
    todo1 = service.add_todo("Buy groceries")
    assert todo1.id == 1
    assert todo1.description == "Buy groceries"
    assert todo1.completed == False
    print("  ✓ Add valid todo")

    # Test trimming whitespace
    todo2 = service.add_todo("  Write report  ")
    assert todo2.description == "Write report"
    print("  ✓ Trim whitespace")

    # Test empty description
    try:
        service.add_todo("")
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "cannot be empty" in str(e)
        print("  ✓ Reject empty description")

    # Test whitespace-only description
    try:
        service.add_todo("   ")
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "cannot be empty" in str(e)
        print("  ✓ Reject whitespace-only description")

    # Test too long description
    try:
        service.add_todo("A" * 1001)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "too long" in str(e)
        print("  ✓ Reject too long description")

    # Test max length description
    todo3 = service.add_todo("A" * 1000)
    assert len(todo3.description) == 1000
    print("  ✓ Accept max length description")

    print("✓ Add Todo tests passed\n")


def test_view_todos():
    """Test viewing todos."""
    print("Testing: View Todos")
    service = TodoService()

    # Test empty list
    todos = service.get_all_todos()
    assert len(todos) == 0
    print("  ✓ View empty list")

    # Test populated list
    service.add_todo("Task 1")
    service.add_todo("Task 2")
    service.add_todo("Task 3")
    todos = service.get_all_todos()
    assert len(todos) == 3
    assert todos[0].id == 1
    assert todos[1].id == 2
    assert todos[2].id == 3
    print("  ✓ View populated list")

    # Test stats
    total, completed, pending = service.get_stats()
    assert total == 3
    assert completed == 0
    assert pending == 3
    print("  ✓ Get stats")

    print("✓ View Todos tests passed\n")


def test_mark_complete():
    """Test marking todos complete."""
    print("Testing: Mark Complete")
    service = TodoService()

    todo1 = service.add_todo("Task 1")
    todo2 = service.add_todo("Task 2")

    # Test mark complete
    service.mark_complete(1)
    assert service.get_todo(1).completed == True
    print("  ✓ Mark todo complete")

    # Test idempotent
    service.mark_complete(1)
    assert service.get_todo(1).completed == True
    print("  ✓ Mark complete is idempotent")

    # Test non-existent ID
    try:
        service.mark_complete(999)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("  ✓ Reject non-existent ID")

    # Test stats after completion
    total, completed, pending = service.get_stats()
    assert total == 2
    assert completed == 1
    assert pending == 1
    print("  ✓ Stats updated correctly")

    print("✓ Mark Complete tests passed\n")


def test_update_todo():
    """Test updating todos."""
    print("Testing: Update Todo")
    service = TodoService()

    todo1 = service.add_todo("Original description")

    # Test valid update
    service.update_todo(1, "Updated description")
    assert service.get_todo(1).description == "Updated description"
    print("  ✓ Update todo description")

    # Test trimming
    service.update_todo(1, "  Trimmed  ")
    assert service.get_todo(1).description == "Trimmed"
    print("  ✓ Trim whitespace in update")

    # Test empty description
    try:
        service.update_todo(1, "")
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "cannot be empty" in str(e)
        print("  ✓ Reject empty description")

    # Test non-existent ID
    try:
        service.update_todo(999, "New description")
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("  ✓ Reject non-existent ID")

    # Test completion status preserved
    service.mark_complete(1)
    service.update_todo(1, "Another update")
    assert service.get_todo(1).completed == True
    print("  ✓ Completion status preserved")

    print("✓ Update Todo tests passed\n")


def test_delete_todo():
    """Test deleting todos."""
    print("Testing: Delete Todo")
    service = TodoService()

    service.add_todo("Task 1")
    service.add_todo("Task 2")
    service.add_todo("Task 3")

    # Test valid delete
    service.delete_todo(2)
    assert service.get_todo(2) is None
    assert len(service.get_all_todos()) == 2
    print("  ✓ Delete todo")

    # Test non-existent ID
    try:
        service.delete_todo(999)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("  ✓ Reject non-existent ID")

    # Test ID not reused
    todo4 = service.add_todo("Task 4")
    assert todo4.id == 4  # Not 2
    print("  ✓ IDs not reused after deletion")

    print("✓ Delete Todo tests passed\n")


def test_todo_display():
    """Test todo string representation."""
    print("Testing: Todo Display")

    # Test incomplete todo
    todo1 = Todo(id=1, description="Test task", completed=False)
    assert str(todo1) == "[ ] 1. Test task"
    print("  ✓ Incomplete todo display")

    # Test completed todo
    todo2 = Todo(id=2, description="Done task", completed=True)
    assert str(todo2) == "[✓] 2. Done task"
    print("  ✓ Completed todo display")

    print("✓ Todo Display tests passed\n")


def test_full_workflow():
    """Test complete user workflow."""
    print("Testing: Full Workflow")
    service = TodoService()

    # Add 3 todos
    service.add_todo("Buy groceries")
    service.add_todo("Write report")
    service.add_todo("Call dentist")
    print("  ✓ Added 3 todos")

    # Mark 1 complete
    service.mark_complete(1)
    total, completed, pending = service.get_stats()
    assert completed == 1
    print("  ✓ Marked 1 complete")

    # Update 1
    service.update_todo(2, "Write quarterly report")
    assert service.get_todo(2).description == "Write quarterly report"
    print("  ✓ Updated 1 todo")

    # Delete 1
    service.delete_todo(3)
    assert len(service.get_all_todos()) == 2
    print("  ✓ Deleted 1 todo")

    # Verify final state
    todos = service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].id == 1
    assert todos[0].completed == True
    assert todos[1].id == 2
    assert todos[1].description == "Write quarterly report"
    print("  ✓ Final state correct")

    print("✓ Full Workflow tests passed\n")


def main():
    """Run all tests."""
    print("=" * 50)
    print("  Phase I Console Todo App - Automated Tests")
    print("=" * 50)
    print()

    try:
        test_add_todo()
        test_view_todos()
        test_mark_complete()
        test_update_todo()
        test_delete_todo()
        test_todo_display()
        test_full_workflow()

        print("=" * 50)
        print("  ✓ ALL TESTS PASSED")
        print("=" * 50)
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
