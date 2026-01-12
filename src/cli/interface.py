"""CLI interface for Phase I Console Todo App.

This module provides the console user interface for interacting with the todo application.
Handles menu display, user input, and output formatting.
"""

import sys
from services.todo_service import TodoService


def display_menu() -> None:
    """Display the main menu with all available options."""
    print("\n" + "=" * 40)
    print("         Todo Application")
    print("=" * 40)
    print("\n1. Add todo")
    print("2. View all todos")
    print("3. Update todo")
    print("4. Delete todo")
    print("5. Mark todo complete")
    print("6. Exit")


def get_menu_choice() -> int:
    """Get and validate menu choice from user.

    Returns:
        Valid menu choice (1-6)

    Displays error message and re-prompts if input is invalid.
    """
    while True:
        try:
            choice = input("\nEnter choice (1-6): ").strip()
            choice_int = int(choice)
            if 1 <= choice_int <= 6:
                return choice_int
            else:
                print("✗ Error: Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("✗ Error: Invalid choice. Please enter a number between 1 and 6.")


def handle_add_todo(service: TodoService) -> None:
    """Handle add todo operation.

    Args:
        service: TodoService instance for managing todos
    """
    print()
    description = input("Enter todo description: ").strip()

    try:
        todo = service.add_todo(description)
        print(f"\n✓ Todo added successfully! (ID: {todo.id})")
    except ValueError as e:
        print(f"\n✗ Error: {e}")


def handle_view_todos(service: TodoService) -> None:
    """Handle view all todos operation.

    Args:
        service: TodoService instance for managing todos
    """
    print("\nYour Todos:")
    print("-" * 40)

    todos = service.get_all_todos()

    if not todos:
        print("No todos yet. Add one to get started!")
    else:
        for todo in todos:
            print(todo)
        print("-" * 40)
        total, completed, pending = service.get_stats()
        print(f"Total: {total} todo{'s' if total != 1 else ''} ({completed} completed, {pending} pending)")


def handle_update_todo(service: TodoService) -> None:
    """Handle update todo operation.

    Args:
        service: TodoService instance for managing todos
    """
    print()
    try:
        todo_id_str = input("Enter todo ID to update: ").strip()
        todo_id = int(todo_id_str)

        # Show current description
        todo = service.get_todo(todo_id)
        if todo is None:
            print(f"\n✗ Error: Todo with ID {todo_id} not found")
            return

        print(f"Current description: {todo.description}")
        new_description = input("Enter new description: ").strip()

        service.update_todo(todo_id, new_description)
        print("\n✓ Todo updated successfully!")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("\n✗ Error: Please enter a valid number")
        else:
            print(f"\n✗ Error: {e}")


def handle_delete_todo(service: TodoService) -> None:
    """Handle delete todo operation.

    Args:
        service: TodoService instance for managing todos
    """
    print()
    try:
        todo_id_str = input("Enter todo ID to delete: ").strip()
        todo_id = int(todo_id_str)

        service.delete_todo(todo_id)
        print("\n✓ Todo deleted successfully!")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("\n✗ Error: Please enter a valid number")
        else:
            print(f"\n✗ Error: {e}")


def handle_mark_complete(service: TodoService) -> None:
    """Handle mark todo complete operation.

    Args:
        service: TodoService instance for managing todos
    """
    print()
    try:
        todo_id_str = input("Enter todo ID to mark complete: ").strip()
        todo_id = int(todo_id_str)

        todo = service.get_todo(todo_id)
        was_completed = todo.completed if todo else False

        service.mark_complete(todo_id)

        if was_completed:
            print("\n✓ Todo marked as complete! (already completed)")
        else:
            print("\n✓ Todo marked as complete!")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("\n✗ Error: Please enter a valid number")
        else:
            print(f"\n✗ Error: {e}")


def run_cli_loop(service: TodoService) -> None:
    """Main CLI loop.

    Args:
        service: TodoService instance for managing todos
    """
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            handle_add_todo(service)
        elif choice == 2:
            handle_view_todos(service)
        elif choice == 3:
            handle_update_todo(service)
        elif choice == 4:
            handle_delete_todo(service)
        elif choice == 5:
            handle_mark_complete(service)
        elif choice == 6:
            print("\nThank you for using Todo Application!")
            print("Goodbye!\n")
            sys.exit(0)
