"""TodoService for Phase I Console Todo App.

This module provides the business logic and CRUD operations for managing todos.
All todos are stored in memory and lost when the application terminates.
"""

from typing import Dict, List, Optional
from models.todo import Todo


class TodoService:
    """Service class for managing todo items.

    Provides CRUD operations (Create, Read, Update, Delete) and completion
    status management for todos. All data is stored in-memory using a dictionary.

    Attributes:
        _todos: Dictionary mapping todo IDs to Todo objects
        _next_id: Counter for generating unique sequential IDs
    """

    def __init__(self):
        """Initialize the TodoService with empty storage."""
        self._todos: Dict[int, Todo] = {}
        self._next_id: int = 1

    def add_todo(self, description: str) -> Todo:
        """Add a new todo item.

        Args:
            description: Text description of the task (must be non-empty)

        Returns:
            The newly created Todo object with assigned ID

        Raises:
            ValueError: If description is empty or exceeds 1000 characters
        """
        # Trim whitespace
        description = description.strip()

        # Validate description
        if not description:
            raise ValueError("Description cannot be empty")
        if len(description) > 1000:
            raise ValueError("Description too long (max 1000 characters)")

        # Create and store todo
        todo = Todo(id=self._next_id, description=description, completed=False)
        self._todos[self._next_id] = todo
        self._next_id += 1

        return todo

    def get_all_todos(self) -> List[Todo]:
        """Get all todos.

        Returns:
            List of all Todo objects, ordered by ID
        """
        return sorted(self._todos.values(), key=lambda t: t.id)

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """Get a specific todo by ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        return self._todos.get(todo_id)

    def update_todo(self, todo_id: int, new_description: str) -> Todo:
        """Update a todo's description.

        Args:
            todo_id: The ID of the todo to update
            new_description: The new description text

        Returns:
            The updated Todo object

        Raises:
            ValueError: If todo not found, or new description is invalid
        """
        # Check if todo exists
        todo = self._todos.get(todo_id)
        if todo is None:
            raise ValueError(f"Todo with ID {todo_id} not found")

        # Trim whitespace
        new_description = new_description.strip()

        # Validate new description
        if not new_description:
            raise ValueError("Description cannot be empty")
        if len(new_description) > 1000:
            raise ValueError("Description too long (max 1000 characters)")

        # Update description
        todo.description = new_description
        return todo

    def delete_todo(self, todo_id: int) -> None:
        """Delete a todo.

        Args:
            todo_id: The ID of the todo to delete

        Raises:
            ValueError: If todo not found
        """
        if todo_id not in self._todos:
            raise ValueError(f"Todo with ID {todo_id} not found")

        del self._todos[todo_id]

    def mark_complete(self, todo_id: int) -> Todo:
        """Mark a todo as complete.

        This operation is idempotent - marking an already-completed todo
        as complete will not raise an error.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            The updated Todo object

        Raises:
            ValueError: If todo not found
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            raise ValueError(f"Todo with ID {todo_id} not found")

        todo.completed = True
        return todo

    def get_stats(self) -> tuple[int, int, int]:
        """Get todo statistics.

        Returns:
            Tuple of (total_count, completed_count, pending_count)
        """
        total = len(self._todos)
        completed = sum(1 for todo in self._todos.values() if todo.completed)
        pending = total - completed
        return (total, completed, pending)
