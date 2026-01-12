"""Main entry point for Phase I Console Todo App.

This module initializes the application and starts the CLI loop.
"""

import sys
import os

# Add src directory to Python path to enable imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.todo_service import TodoService
from cli.interface import run_cli_loop


def main():
    """Initialize and run the todo application."""
    # Create service instance
    service = TodoService()

    # Start CLI loop
    try:
        run_cli_loop(service)
    except KeyboardInterrupt:
        print("\n\nThank you for using Todo Application!")
        print("Goodbye!\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
