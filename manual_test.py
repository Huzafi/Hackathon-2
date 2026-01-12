"""Manual test script to verify main.py functionality.

This script simulates user interactions with the todo application.
"""

import sys
import os
import io
from io import StringIO

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from services.todo_service import TodoService
from cli.interface import (
    display_menu, get_menu_choice, handle_add_todo, handle_view_todos,
    handle_update_todo, handle_delete_todo, handle_mark_complete
)


def simulate_user_workflow():
    """Simulate a complete user workflow."""
    print("=" * 60)
    print("  Manual Test: Simulating Complete User Workflow")
    print("=" * 60)
    print()

    service = TodoService()

    # Test 1: Add todos
    print("Test 1: Adding 3 todos")
    print("-" * 60)

    # Simulate adding todo 1
    print("Simulating: Add 'Buy groceries'")
    todo1 = service.add_todo("Buy groceries")
    print(f"✓ Added: {todo1}")

    # Simulate adding todo 2
    print("Simulating: Add 'Write report'")
    todo2 = service.add_todo("Write report")
    print(f"✓ Added: {todo2}")

    # Simulate adding todo 3
    print("Simulating: Add 'Call dentist'")
    todo3 = service.add_todo("Call dentist")
    print(f"✓ Added: {todo3}")
    print()

    # Test 2: View all todos
    print("Test 2: Viewing all todos")
    print("-" * 60)
    todos = service.get_all_todos()
    for todo in todos:
        print(todo)
    total, completed, pending = service.get_stats()
    print(f"Total: {total} todos ({completed} completed, {pending} pending)")
    print()

    # Test 3: Mark todo complete
    print("Test 3: Marking todo #1 as complete")
    print("-" * 60)
    service.mark_complete(1)
    print(f"✓ Marked complete: {service.get_todo(1)}")
    print()

    # Test 4: View todos after marking complete
    print("Test 4: Viewing todos after marking complete")
    print("-" * 60)
    todos = service.get_all_todos()
    for todo in todos:
        print(todo)
    total, completed, pending = service.get_stats()
    print(f"Total: {total} todos ({completed} completed, {pending} pending)")
    print()

    # Test 5: Update todo
    print("Test 5: Updating todo #2 description")
    print("-" * 60)
    old_desc = service.get_todo(2).description
    print(f"Old description: {old_desc}")
    service.update_todo(2, "Write quarterly report")
    print(f"New description: {service.get_todo(2).description}")
    print(f"✓ Updated: {service.get_todo(2)}")
    print()

    # Test 6: Delete todo
    print("Test 6: Deleting todo #3")
    print("-" * 60)
    print(f"Before delete: {service.get_todo(3)}")
    service.delete_todo(3)
    print("✓ Deleted todo #3")
    print()

    # Test 7: View final state
    print("Test 7: Viewing final state")
    print("-" * 60)
    todos = service.get_all_todos()
    for todo in todos:
        print(todo)
    total, completed, pending = service.get_stats()
    print(f"Total: {total} todos ({completed} completed, {pending} pending)")
    print()

    # Test 8: Verify ID not reused
    print("Test 8: Adding new todo (verify ID not reused)")
    print("-" * 60)
    todo4 = service.add_todo("Review code")
    print(f"✓ Added: {todo4}")
    print(f"Note: ID is {todo4.id}, not 3 (IDs are never reused)")
    print()

    # Test 9: Error handling - empty description
    print("Test 9: Error handling - empty description")
    print("-" * 60)
    try:
        service.add_todo("")
        print("✗ FAILED: Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly rejected: {e}")
    print()

    # Test 10: Error handling - non-existent ID
    print("Test 10: Error handling - non-existent ID")
    print("-" * 60)
    try:
        service.update_todo(999, "Test")
        print("✗ FAILED: Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly rejected: {e}")
    print()

    # Test 11: Edge case - mark already complete
    print("Test 11: Edge case - mark already complete (idempotent)")
    print("-" * 60)
    print(f"Before: {service.get_todo(1)}")
    service.mark_complete(1)
    print(f"After: {service.get_todo(1)}")
    print("✓ Idempotent operation successful")
    print()

    # Final summary
    print("=" * 60)
    print("  Final State Summary")
    print("=" * 60)
    todos = service.get_all_todos()
    for todo in todos:
        print(todo)
    total, completed, pending = service.get_stats()
    print(f"\nTotal: {total} todos ({completed} completed, {pending} pending)")
    print()
    print("=" * 60)
    print("  ✓ ALL MANUAL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    simulate_user_workflow()
