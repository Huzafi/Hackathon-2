# Data Model: Phase I Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-12
**Phase**: 1 - Design

## Overview

This document defines the data model for the Phase I console todo application. The model is designed to be simple, maintainable, and extensible for Phase II migration to database-backed storage.

## Entities

### Todo

Represents a single task item in the todo list.

**Attributes**:

| Attribute | Type | Required | Description | Validation Rules |
|-----------|------|----------|-------------|------------------|
| `id` | int | Yes | Unique identifier for the todo | Positive integer, auto-generated, never reused |
| `description` | str | Yes | Text description of the task | Non-empty, max 1000 characters |
| `completed` | bool | Yes | Completion status of the todo | True (complete) or False (incomplete), defaults to False |

**Relationships**: None (single entity model)

**State Transitions**:
- **Created**: `completed = False` (default state)
- **Marked Complete**: `completed = True` (idempotent operation)
- **Updated**: `description` can change, `completed` status preserved
- **Deleted**: Entity removed from storage

**Invariants**:
- `id` is immutable once assigned
- `description` cannot be empty string
- `completed` is always a boolean (no null/undefined states)

## Storage Structure

**In-Memory Representation** (Phase I):
```python
# Dictionary with integer keys (todo IDs) and Todo objects as values
todos: dict[int, Todo] = {
    1: Todo(id=1, description="Buy groceries", completed=False),
    2: Todo(id=2, description="Write report", completed=True),
    3: Todo(id=3, description="Call dentist", completed=False)
}

# Counter for next available ID
next_id: int = 4
```

**Phase II Migration Path**:
```python
# SQLModel table definition (Phase II)
from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str = Field(max_length=1000)
    completed: bool = Field(default=False)
```

## Validation Rules

### Description Validation
- **Non-empty**: Must contain at least 1 character
- **Max length**: 1000 characters (prevents memory issues)
- **Trimming**: Leading/trailing whitespace should be trimmed
- **Error message**: "Description cannot be empty" or "Description too long (max 1000 characters)"

### ID Validation
- **Existence check**: ID must exist in storage for update/delete/complete operations
- **Type check**: Must be a valid integer
- **Error message**: "Todo with ID {id} not found"

### Completion Status
- **Type check**: Must be boolean (True/False)
- **Idempotent**: Marking an already-completed todo as complete is allowed (no error)

## Example Data

### Empty State
```python
todos = {}
next_id = 1
```

### Populated State
```python
todos = {
    1: Todo(id=1, description="Buy groceries", completed=False),
    2: Todo(id=2, description="Write report", completed=True),
    3: Todo(id=3, description="Call dentist", completed=False),
    5: Todo(id=5, description="Review code", completed=False)
}
next_id = 6  # Note: ID 4 was deleted, not reused
```

## Edge Cases

1. **Empty description after trimming**: Reject with error
2. **Very long description (>1000 chars)**: Reject with error
3. **Special characters in description**: Allow (no sanitization needed for console display)
4. **Duplicate descriptions**: Allow (IDs are unique, descriptions can repeat)
5. **Deleted ID gaps**: IDs are never reused, gaps are expected
6. **Integer overflow**: Not a concern for Phase I (Python handles arbitrary precision)

## Implementation Notes

### Python Class Definition (Phase I)

```python
from dataclasses import dataclass

@dataclass
class Todo:
    """Represents a single todo item."""
    id: int
    description: str
    completed: bool = False

    def __str__(self) -> str:
        """String representation for display."""
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.description}"
```

### Alternative: Simple Class

```python
class Todo:
    """Represents a single todo item."""

    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        """String representation for display."""
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.description}"
```

## Testing Considerations

### Valid Todo Creation
- ID: 1, Description: "Test task", Completed: False
- ID: 100, Description: "A" * 1000, Completed: True

### Invalid Todo Creation
- Description: "" (empty)
- Description: "A" * 1001 (too long)
- ID: -1 (negative, though auto-generated so unlikely)

### State Transitions
- Create → View: Todo appears in list
- Create → Complete → View: Status shows as completed
- Create → Update → View: Description changes
- Create → Delete → View: Todo no longer appears

## References

- Feature Specification: `specs/001-console-todo-app/spec.md`
- Research Document: `specs/001-console-todo-app/research.md`
- Implementation Plan: `specs/001-console-todo-app/plan.md`
