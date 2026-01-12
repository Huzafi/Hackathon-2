# CLI Interface Contract: Phase I Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-12
**Phase**: 1 - Design

## Overview

This document specifies the command-line interface contract for the Phase I console todo application. It defines the menu structure, user interactions, input/output formats, and error handling behavior.

## Main Menu

### Display Format

```
========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): _
```

### Menu Behavior

- Display menu after each operation completes
- Accept numeric input (1-6)
- Invalid input displays error and re-prompts
- Menu persists until user selects "6. Exit"

---

## Operation 1: Add Todo

### User Flow

```
Enter choice (1-6): 1

Enter todo description: Buy groceries

✓ Todo added successfully! (ID: 1)

[Return to main menu]
```

### Input Validation

| Input | Validation | Error Message |
|-------|------------|---------------|
| Empty description | Reject | "Error: Description cannot be empty" |
| Whitespace only | Reject (after trim) | "Error: Description cannot be empty" |
| >1000 characters | Reject | "Error: Description too long (max 1000 characters)" |
| Valid description | Accept | Success message with assigned ID |

### Success Response

```
✓ Todo added successfully! (ID: {id})
```

---

## Operation 2: View All Todos

### User Flow (With Todos)

```
Enter choice (1-6): 2

Your Todos:
----------------------------------------
[ ] 1. Buy groceries
[✓] 2. Write report
[ ] 3. Call dentist
----------------------------------------
Total: 3 todos (1 completed, 2 pending)

[Return to main menu]
```

### User Flow (Empty List)

```
Enter choice (1-6): 2

Your Todos:
----------------------------------------
No todos yet. Add one to get started!
----------------------------------------

[Return to main menu]
```

### Display Format

- `[ ]` = Incomplete todo
- `[✓]` = Completed todo
- Show ID, description for each todo
- Display summary: total count, completed count, pending count

---

## Operation 3: Update Todo

### User Flow (Success)

```
Enter choice (1-6): 3

Enter todo ID to update: 1
Current description: Buy groceries
Enter new description: Buy organic groceries

✓ Todo updated successfully!

[Return to main menu]
```

### User Flow (Invalid ID)

```
Enter choice (1-6): 3

Enter todo ID to update: 99

✗ Error: Todo with ID 99 not found

[Return to main menu]
```

### Input Validation

| Input | Validation | Error Message |
|-------|------------|---------------|
| Non-numeric ID | Reject | "Error: Please enter a valid number" |
| Non-existent ID | Reject | "Error: Todo with ID {id} not found" |
| Empty new description | Reject | "Error: Description cannot be empty" |
| Valid ID + description | Accept | Success message |

### Success Response

```
✓ Todo updated successfully!
```

---

## Operation 4: Delete Todo

### User Flow (Success)

```
Enter choice (1-6): 4

Enter todo ID to delete: 2

✓ Todo deleted successfully!

[Return to main menu]
```

### User Flow (Invalid ID)

```
Enter choice (1-6): 4

Enter todo ID to delete: 99

✗ Error: Todo with ID 99 not found

[Return to main menu]
```

### Input Validation

| Input | Validation | Error Message |
|-------|------------|---------------|
| Non-numeric ID | Reject | "Error: Please enter a valid number" |
| Non-existent ID | Reject | "Error: Todo with ID {id} not found" |
| Valid ID | Accept | Success message |

### Success Response

```
✓ Todo deleted successfully!
```

---

## Operation 5: Mark Todo Complete

### User Flow (Success)

```
Enter choice (1-6): 5

Enter todo ID to mark complete: 1

✓ Todo marked as complete!

[Return to main menu]
```

### User Flow (Already Complete)

```
Enter choice (1-6): 5

Enter todo ID to mark complete: 2

✓ Todo marked as complete! (already completed)

[Return to main menu]
```

### User Flow (Invalid ID)

```
Enter choice (1-6): 5

Enter todo ID to mark complete: 99

✗ Error: Todo with ID 99 not found

[Return to main menu]
```

### Input Validation

| Input | Validation | Error Message |
|-------|------------|---------------|
| Non-numeric ID | Reject | "Error: Please enter a valid number" |
| Non-existent ID | Reject | "Error: Todo with ID {id} not found" |
| Valid ID | Accept | Success message (idempotent) |

### Success Response

```
✓ Todo marked as complete!
```

---

## Operation 6: Exit

### User Flow

```
Enter choice (1-6): 6

Thank you for using Todo Application!
Goodbye!

[Application terminates]
```

### Behavior

- Display goodbye message
- Exit cleanly (no errors)
- All in-memory data is lost (expected behavior)

---

## Error Handling

### Invalid Menu Choice

```
Enter choice (1-6): 9

✗ Error: Invalid choice. Please enter a number between 1 and 6.

[Re-display menu]
```

### Non-Numeric Menu Input

```
Enter choice (1-6): abc

✗ Error: Invalid choice. Please enter a number between 1 and 6.

[Re-display menu]
```

### General Error Format

```
✗ Error: {error_message}
```

- Prefix with "✗ Error:" for visibility
- Clear, actionable error messages
- No stack traces or technical details shown to user

---

## Input/Output Specifications

### Input Handling

- **Prompt format**: `{prompt_text}: _` (with trailing space)
- **Input method**: `input()` function (blocking, waits for Enter)
- **Trimming**: Strip leading/trailing whitespace from all inputs
- **Case sensitivity**: Menu choices are numeric (case N/A), descriptions preserve case

### Output Formatting

- **Success messages**: Prefix with "✓" (checkmark)
- **Error messages**: Prefix with "✗" (cross mark)
- **Separators**: Use "========" (40 chars) for headers, "--------" (40 chars) for sections
- **Alignment**: Left-aligned text
- **Line breaks**: Single blank line between sections

### Color/Styling (Optional)

- Success messages: Green text (if terminal supports ANSI)
- Error messages: Red text (if terminal supports ANSI)
- Fallback: Plain text with symbols (✓/✗)

---

## Example Session

```
========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): 1

Enter todo description: Buy groceries

✓ Todo added successfully! (ID: 1)

========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): 1

Enter todo description: Write report

✓ Todo added successfully! (ID: 2)

========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): 2

Your Todos:
----------------------------------------
[ ] 1. Buy groceries
[ ] 2. Write report
----------------------------------------
Total: 2 todos (0 completed, 2 pending)

========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): 5

Enter todo ID to mark complete: 1

✓ Todo marked as complete!

========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): 2

Your Todos:
----------------------------------------
[✓] 1. Buy groceries
[ ] 2. Write report
----------------------------------------
Total: 2 todos (1 completed, 1 pending)

========================================
         Todo Application
========================================

1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6): 6

Thank you for using Todo Application!
Goodbye!
```

---

## Implementation Notes

### CLI Module Structure

```python
# src/cli/interface.py

def display_menu() -> None:
    """Display the main menu."""
    pass

def get_menu_choice() -> int:
    """Get and validate menu choice from user."""
    pass

def handle_add_todo(service: TodoService) -> None:
    """Handle add todo operation."""
    pass

def handle_view_todos(service: TodoService) -> None:
    """Handle view all todos operation."""
    pass

def handle_update_todo(service: TodoService) -> None:
    """Handle update todo operation."""
    pass

def handle_delete_todo(service: TodoService) -> None:
    """Handle delete todo operation."""
    pass

def handle_mark_complete(service: TodoService) -> None:
    """Handle mark todo complete operation."""
    pass

def run_cli_loop(service: TodoService) -> None:
    """Main CLI loop."""
    pass
```

---

## Testing Checklist

- [ ] Menu displays correctly
- [ ] All 6 menu options work
- [ ] Invalid menu choices show error
- [ ] Add todo with valid description succeeds
- [ ] Add todo with empty description fails
- [ ] View todos shows all items correctly
- [ ] View todos on empty list shows appropriate message
- [ ] Update todo with valid ID and description succeeds
- [ ] Update todo with invalid ID fails
- [ ] Delete todo with valid ID succeeds
- [ ] Delete todo with invalid ID fails
- [ ] Mark complete with valid ID succeeds
- [ ] Mark complete with invalid ID fails
- [ ] Mark complete on already-completed todo is idempotent
- [ ] Exit option terminates application cleanly

---

## References

- Feature Specification: `specs/001-console-todo-app/spec.md`
- Data Model: `specs/001-console-todo-app/data-model.md`
- Research Document: `specs/001-console-todo-app/research.md`
