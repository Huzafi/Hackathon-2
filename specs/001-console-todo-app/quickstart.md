# Quickstart Guide: Phase I Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-12
**Phase**: 1 - Design

## Overview

This guide provides step-by-step instructions for setting up, running, and testing the Phase I console todo application. It covers environment setup, application usage, and manual testing procedures.

## Prerequisites

- Python 3.13 or higher installed
- UV package manager installed
- Terminal/console access (Windows/Linux/macOS)

## Setup Instructions

### 1. Clone Repository (if applicable)

```bash
git clone <repository-url>
cd Hackathon-Phase-2
```

### 2. Initialize UV Environment

```bash
# Create UV project (if not already initialized)
uv init

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Verify Python Version

```bash
python --version
# Should show Python 3.13.x or higher
```

### 4. Project Structure

Ensure the following structure exists:

```
Hackathon-Phase-2/
├── src/
│   ├── models/
│   │   └── todo.py
│   ├── services/
│   │   └── todo_service.py
│   ├── cli/
│   │   └── interface.py
│   └── main.py
├── pyproject.toml
└── README.md
```

## Running the Application

### Start the Application

```bash
# From repository root
python src/main.py
```

### Expected Output

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

## Usage Examples

### Example 1: Add and View Todos

```
Enter choice (1-6): 1
Enter todo description: Buy groceries
✓ Todo added successfully! (ID: 1)

Enter choice (1-6): 1
Enter todo description: Write report
✓ Todo added successfully! (ID: 2)

Enter choice (1-6): 2
Your Todos:
----------------------------------------
[ ] 1. Buy groceries
[ ] 2. Write report
----------------------------------------
Total: 2 todos (0 completed, 2 pending)
```

### Example 2: Mark Todo Complete

```
Enter choice (1-6): 5
Enter todo ID to mark complete: 1
✓ Todo marked as complete!

Enter choice (1-6): 2
Your Todos:
----------------------------------------
[✓] 1. Buy groceries
[ ] 2. Write report
----------------------------------------
Total: 2 todos (1 completed, 1 pending)
```

### Example 3: Update Todo

```
Enter choice (1-6): 3
Enter todo ID to update: 2
Current description: Write report
Enter new description: Write quarterly report
✓ Todo updated successfully!
```

### Example 4: Delete Todo

```
Enter choice (1-6): 4
Enter todo ID to delete: 1
✓ Todo deleted successfully!

Enter choice (1-6): 2
Your Todos:
----------------------------------------
[ ] 2. Write quarterly report
----------------------------------------
Total: 1 todo (0 completed, 1 pending)
```

### Example 5: Exit Application

```
Enter choice (1-6): 6
Thank you for using Todo Application!
Goodbye!
```

## Manual Testing Checklist

### Basic Operations ✅

- [ ] **Test 1: Add Todo**
  - Action: Add todo with description "Test task 1"
  - Expected: Success message with ID 1
  - Verify: Todo appears in view list

- [ ] **Test 2: View Empty List**
  - Action: View todos when list is empty
  - Expected: "No todos yet" message
  - Verify: No errors, clean display

- [ ] **Test 3: View Populated List**
  - Action: Add 3 todos, then view
  - Expected: All 3 todos displayed with IDs, descriptions, status
  - Verify: Correct count summary

- [ ] **Test 4: Mark Complete**
  - Action: Mark todo ID 1 as complete
  - Expected: Success message
  - Verify: Status shows [✓] in view list

- [ ] **Test 5: Update Todo**
  - Action: Update todo ID 2 description
  - Expected: Success message
  - Verify: New description appears in view list

- [ ] **Test 6: Delete Todo**
  - Action: Delete todo ID 3
  - Expected: Success message
  - Verify: Todo no longer appears in view list

### Error Handling ✅

- [ ] **Test 7: Empty Description**
  - Action: Add todo with empty description
  - Expected: Error message "Description cannot be empty"
  - Verify: No todo created

- [ ] **Test 8: Invalid Menu Choice**
  - Action: Enter "9" at main menu
  - Expected: Error message "Invalid choice"
  - Verify: Menu re-displays

- [ ] **Test 9: Non-Numeric Menu Input**
  - Action: Enter "abc" at main menu
  - Expected: Error message "Invalid choice"
  - Verify: Menu re-displays

- [ ] **Test 10: Non-Existent Todo ID (Update)**
  - Action: Update todo ID 999
  - Expected: Error message "Todo with ID 999 not found"
  - Verify: No changes to existing todos

- [ ] **Test 11: Non-Existent Todo ID (Delete)**
  - Action: Delete todo ID 999
  - Expected: Error message "Todo with ID 999 not found"
  - Verify: No changes to existing todos

- [ ] **Test 12: Non-Existent Todo ID (Mark Complete)**
  - Action: Mark complete todo ID 999
  - Expected: Error message "Todo with ID 999 not found"
  - Verify: No changes to existing todos

### Edge Cases ✅

- [ ] **Test 13: Long Description**
  - Action: Add todo with 1000 character description
  - Expected: Success (at limit)
  - Verify: Full description stored and displayed

- [ ] **Test 14: Too Long Description**
  - Action: Add todo with 1001 character description
  - Expected: Error message "Description too long"
  - Verify: No todo created

- [ ] **Test 15: Whitespace-Only Description**
  - Action: Add todo with "   " (spaces only)
  - Expected: Error message "Description cannot be empty"
  - Verify: No todo created

- [ ] **Test 16: Special Characters**
  - Action: Add todo with "Test @#$% & *() task"
  - Expected: Success
  - Verify: Special characters preserved

- [ ] **Test 17: Duplicate Descriptions**
  - Action: Add two todos with same description
  - Expected: Both succeed with different IDs
  - Verify: Both appear in list

- [ ] **Test 18: Mark Already Complete**
  - Action: Mark complete on already-completed todo
  - Expected: Success (idempotent)
  - Verify: Status remains complete

- [ ] **Test 19: ID Gaps After Deletion**
  - Action: Add 3 todos, delete ID 2, add another
  - Expected: New todo gets ID 4 (not reusing ID 2)
  - Verify: IDs are 1, 3, 4

- [ ] **Test 20: Large Number of Todos**
  - Action: Add 100 todos
  - Expected: All operations remain fast (<5 seconds)
  - Verify: View list displays all 100

### Full Workflow ✅

- [ ] **Test 21: Complete User Journey**
  - Action: Add 3 todos → Mark 1 complete → Update 1 → Delete 1 → View list
  - Expected: All operations succeed
  - Verify: Final state matches expected (2 todos, 1 complete)
  - Time: Should complete in under 2 minutes

## Troubleshooting

### Issue: "Python not found"

**Solution**: Ensure Python 3.13+ is installed and in PATH

```bash
# Check Python installation
python --version

# If not found, install Python 3.13+ from python.org
```

### Issue: "Module not found" errors

**Solution**: Ensure you're running from repository root and structure is correct

```bash
# Verify you're in correct directory
pwd  # Should show Hackathon-Phase-2

# Check structure
ls src/
# Should show: models/ services/ cli/ main.py
```

### Issue: "UV not found"

**Solution**: Install UV package manager

```bash
# Install UV (see UV documentation for platform-specific instructions)
pip install uv
```

### Issue: Application crashes on invalid input

**Solution**: This indicates a bug in error handling. Check:
- Input validation in CLI layer
- Try-except blocks around user input
- Error messages are displayed instead of exceptions

## Performance Expectations

- **Startup time**: <1 second
- **Add todo**: <1 second
- **View todos (100 items)**: <2 seconds
- **Update/Delete/Complete**: <1 second
- **Memory usage**: <50 MB for 100 todos

## Known Limitations (Phase I)

- **No persistence**: All data lost when application exits
- **Single user**: No multi-user support
- **No undo**: Deleted todos cannot be recovered
- **No search**: Must view full list to find todos
- **No categories**: All todos in single flat list
- **No due dates**: Cannot set deadlines
- **Console only**: No web or GUI interface

These limitations are intentional for Phase I and will be addressed in later phases.

## Next Steps

After completing manual testing:

1. **Document Issues**: Record any bugs or unexpected behavior
2. **Verify Constitution Compliance**: Ensure no Phase II features leaked in
3. **Prepare for Phase II**: Review migration path in research.md
4. **Run `/sp.tasks`**: Generate implementation tasks from this plan

## References

- Feature Specification: `specs/001-console-todo-app/spec.md`
- Implementation Plan: `specs/001-console-todo-app/plan.md`
- Data Model: `specs/001-console-todo-app/data-model.md`
- CLI Interface Contract: `specs/001-console-todo-app/contracts/cli-interface.md`
- Research Document: `specs/001-console-todo-app/research.md`

## Support

For issues or questions:
- Review specification documents in `specs/001-console-todo-app/`
- Check constitution for Phase I constraints: `.specify/memory/constitution.md`
- Verify against acceptance scenarios in spec.md
