"""Todo model for Phase I Console Todo App.

This module defines the Todo data structure representing a single task item.
"""

from dataclasses import dataclass


@dataclass
class Todo:
    """Represents a single todo item.

    Attributes:
        id: Unique identifier for the todo (auto-generated, never reused)
        description: Text description of the task (non-empty, max 1000 chars)
        completed: Completion status (True = complete, False = incomplete)
    """
    id: int
    description: str
    completed: bool = False

    def __str__(self) -> str:
        """String representation for display.

        Returns:
            Formatted string with completion status, ID, and description.
            Format: "[✓] 1. Buy groceries" or "[ ] 2. Write report"
        """
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.description}"
