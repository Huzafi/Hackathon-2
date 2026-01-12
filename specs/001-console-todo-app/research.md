# Research: Phase I Console Todo App

**Feature**: 001-console-todo-app
**Date**: 2026-01-12
**Phase**: 0 - Research & Architecture Decisions

## Overview

This document captures the research findings and architectural decisions for the Phase I in-memory console todo application. Since the requirements are well-defined and the technology stack is constrained by the constitution, this research focuses on design patterns and best practices for building a maintainable, extensible console application.

## Key Decisions

### Decision 1: In-Memory Storage Structure

**Decision**: Use a Python dictionary with integer keys for todo storage

**Rationale**:
- Dictionary provides O(1) lookup by ID for all operations (get, update, delete, mark complete)
- Integer keys (1, 2, 3...) are user-friendly and match the sequential ID requirement
- Simple to implement and reason about
- Easy to migrate to database models in Phase II (dict → database table)

**Alternatives Considered**:
- **List with index-based access**: Rejected because deleting items would require re-indexing or leave gaps
- **List with linear search by ID**: Rejected due to O(n) lookup performance (though acceptable for 100 todos)
- **Custom data structure**: Rejected as over-engineering for Phase I requirements

**Implementation Notes**:
- Use a counter variable to track the next available ID
- IDs are never reused (even after deletion) to avoid confusion
- Dictionary keys are integers, values are Todo objects

---

### Decision 2: Separation of Concerns Architecture

**Decision**: Three-layer architecture (Model, Service, CLI)

**Rationale**:
- **Models layer**: Pure data structures with no business logic (easy to adapt to SQLModel in Phase II)
- **Services layer**: Business logic and CRUD operations (can become FastAPI endpoints in Phase II)
- **CLI layer**: User interface and I/O handling (will be replaced by web UI in Phase II)
- Clear boundaries enable independent testing and future migration

**Alternatives Considered**:
- **Single-file monolith**: Rejected because it violates modularity principle and makes Phase II migration harder
- **More complex layering (Repository pattern, etc.)**: Rejected as over-engineering for in-memory storage

**Implementation Notes**:
- Models: Simple dataclass or class with `__init__`
- Services: Stateful class holding the todo dictionary
- CLI: Stateless functions for display and input handling

---

### Decision 3: CLI Interface Pattern

**Decision**: Numbered menu with command loop

**Rationale**:
- User-friendly for non-technical users
- Clear visual feedback for available operations
- Easy to extend with new operations
- Standard pattern for console applications

**Alternatives Considered**:
- **Command-line arguments (e.g., `todo add "Buy milk"`)**: Rejected because it requires multiple invocations and doesn't support interactive workflows
- **Natural language commands**: Rejected as out of scope for Phase I (reserved for Phase III AI chatbot)
- **Single-letter commands (a/v/u/d/c)**: Rejected as less discoverable than numbered menu

**Implementation Notes**:
```
Todo Application
1. Add todo
2. View all todos
3. Update todo
4. Delete todo
5. Mark todo complete
6. Exit

Enter choice (1-6):
```

---

### Decision 4: Error Handling Strategy

**Decision**: Validate input early, display clear error messages, continue execution

**Rationale**:
- Prevents invalid state from entering the system
- User-friendly error messages improve usability
- Application continues running after errors (no crashes)
- Aligns with "Correctness of Behavior" principle

**Alternatives Considered**:
- **Exception-based flow control**: Rejected as it complicates the CLI loop
- **Silent failures**: Rejected as it violates user experience requirements

**Implementation Notes**:
- Validate menu choices (1-6 only)
- Validate todo IDs (must exist in dictionary)
- Validate descriptions (non-empty, reasonable length)
- Display error in red or with clear prefix: "Error: ..."

---

### Decision 5: Todo ID Generation

**Decision**: Sequential integer IDs starting from 1, never reused

**Rationale**:
- Simple and predictable for users
- Matches user mental model (first todo is #1, second is #2, etc.)
- No collision risk
- Easy to implement with a counter

**Alternatives Considered**:
- **UUID**: Rejected as overkill for in-memory single-user app
- **Reuse deleted IDs**: Rejected to avoid user confusion (if todo #3 is deleted, next todo is #4, not #3)

**Implementation Notes**:
- Maintain `next_id` counter in TodoService
- Increment after each add operation
- Counter persists only during application runtime

---

### Decision 6: Testing Strategy

**Decision**: Manual CLI testing for Phase I, optional automated tests

**Rationale**:
- Constitution specifies "Manual CLI validation" as acceptable
- Automated testing adds complexity without immediate value for demo
- Focus on working functionality over test coverage
- Tests can be added later if needed

**Alternatives Considered**:
- **TDD with full test suite**: Rejected as over-engineering for Phase I scope
- **No testing**: Rejected as it violates quality principles

**Implementation Notes**:
- Create manual test checklist in quickstart.md
- If automated tests are added, use pytest with simple assertions
- Focus on integration tests (full CLI workflows) over unit tests

---

### Decision 7: Dependency Management

**Decision**: Use UV for environment management, no external libraries

**Rationale**:
- UV is specified in requirements (Python 3.13+, UV for environment management)
- No external libraries needed for core functionality (Python stdlib sufficient)
- Minimal dependencies align with "Tool-Appropriate Design" principle

**Alternatives Considered**:
- **pip + venv**: Rejected because UV is explicitly required
- **External CLI libraries (click, typer)**: Rejected as unnecessary for simple menu interface

**Implementation Notes**:
- Create pyproject.toml with UV configuration
- No dependencies in `[project.dependencies]` section
- Optional dev dependencies: pytest (if automated tests added)

---

## Technology Stack Summary

| Component | Technology | Justification |
|-----------|------------|---------------|
| Language | Python 3.13+ | Constitution requirement |
| Environment | UV | Specification requirement |
| Storage | In-memory dict | Phase I constraint (no persistence) |
| CLI Framework | Python stdlib (input/print) | Simplicity principle |
| Data Model | Python dataclass or class | Minimal, extensible to SQLModel |
| Testing | Manual + optional pytest | Appropriate for Phase I scope |

---

## Phase II Migration Path

The architecture decisions support clean migration to Phase II:

1. **Models** (`src/models/todo.py`):
   - Add SQLModel inheritance: `class Todo(SQLModel, table=True)`
   - Add database fields: `id: Optional[int] = Field(default=None, primary_key=True)`
   - Core structure remains unchanged

2. **Services** (`src/services/todo_service.py`):
   - Replace in-memory dict with database session
   - CRUD operations become database queries
   - Business logic remains unchanged

3. **CLI** (`src/cli/interface.py`):
   - Replace with FastAPI endpoints
   - Input validation logic can be reused
   - Display logic becomes JSON responses

4. **Entry Point** (`src/main.py`):
   - Replace CLI loop with FastAPI app initialization
   - Service instantiation becomes dependency injection

---

## Open Questions

None. All technical decisions are resolved and aligned with constitution requirements.

---

## References

- Feature Specification: `specs/001-console-todo-app/spec.md`
- Constitution: `.specify/memory/constitution.md`
- Implementation Plan: `specs/001-console-todo-app/plan.md`
