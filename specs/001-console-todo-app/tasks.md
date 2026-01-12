---

description: "Task list for Phase I Console Todo App implementation"
---

# Tasks: Phase I Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/cli-interface.md

**Tests**: Tests are OPTIONAL for Phase I. Manual CLI validation is the primary testing approach per plan.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure (src/models/, src/services/, src/cli/, tests/)
- [X] T002 Initialize UV project with pyproject.toml (Python 3.13+, no external dependencies)
- [X] T003 Create README.md with project overview and usage instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Todo model class in src/models/todo.py (id: int, description: str, completed: bool = False)
- [X] T005 Create TodoService class in src/services/todo_service.py (initialize with empty dict and next_id counter)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Users can add new todo items and view all existing todos in a list format

**Independent Test**: Launch app, add 2-3 todos with different descriptions, view list, verify all todos appear correctly with IDs and completion status

### Implementation for User Story 1

- [X] T006 [P] [US1] Implement add_todo method in src/services/todo_service.py (validate description, assign ID, store in dict)
- [X] T007 [P] [US1] Implement get_all_todos method in src/services/todo_service.py (return list of all todos)
- [X] T008 [US1] Implement display_menu function in src/cli/interface.py (show 6 menu options with formatting)
- [X] T009 [US1] Implement get_menu_choice function in src/cli/interface.py (validate numeric input 1-6)
- [X] T010 [US1] Implement handle_add_todo function in src/cli/interface.py (prompt for description, call service, display confirmation)
- [X] T011 [US1] Implement handle_view_todos function in src/cli/interface.py (get todos from service, format and display with status)
- [X] T012 [US1] Create src/main.py with CLI loop (initialize service, display menu, handle options 1-2 and 6)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently (MVP complete!)

---

## Phase 4: User Story 2 - Mark Todos Complete (Priority: P2)

**Goal**: Users can mark existing todos as complete to track progress

**Independent Test**: Add 3 todos (using P1 functionality), mark 2 as complete, view list, verify completion status correctly displayed

### Implementation for User Story 2

- [X] T013 [US2] Implement mark_complete method in src/services/todo_service.py (find todo by ID, set completed=True, handle not found)
- [X] T014 [US2] Implement handle_mark_complete function in src/cli/interface.py (prompt for ID, call service, display confirmation)
- [X] T015 [US2] Update src/main.py CLI loop to include option 5 (mark complete) in menu handling

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo Descriptions (Priority: P3)

**Goal**: Users can edit the description of existing todos

**Independent Test**: Add 2 todos, update description of one, view list, verify updated description appears correctly while other todo unchanged

### Implementation for User Story 3

- [X] T016 [US3] Implement update_todo method in src/services/todo_service.py (find todo by ID, validate new description, update, handle not found)
- [X] T017 [US3] Implement handle_update_todo function in src/cli/interface.py (prompt for ID and new description, call service, display confirmation)
- [X] T018 [US3] Update src/main.py CLI loop to include option 3 (update) in menu handling

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Todos (Priority: P4)

**Goal**: Users can remove todos from the list when no longer needed

**Independent Test**: Add 4 todos, delete 2 of them (one by one), view list, verify only remaining 2 todos appear

### Implementation for User Story 4

- [X] T019 [US4] Implement delete_todo method in src/services/todo_service.py (find todo by ID, remove from dict, handle not found)
- [X] T020 [US4] Implement handle_delete_todo function in src/cli/interface.py (prompt for ID, call service, display confirmation)
- [X] T021 [US4] Update src/main.py CLI loop to include option 4 (delete) in menu handling

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T022 Add input validation to get_menu_choice in src/cli/interface.py (handle non-numeric input, out of range)
- [X] T023 Add description validation to handle_add_todo in src/cli/interface.py (empty check, length check, trim whitespace)
- [X] T024 Add description validation to handle_update_todo in src/cli/interface.py (empty check, length check, trim whitespace)
- [X] T025 Add ID validation to all CLI handlers in src/cli/interface.py (non-numeric input handling)
- [X] T026 Implement exit functionality in src/main.py (option 6, display goodbye message, clean exit)
- [X] T027 Add error message formatting to src/cli/interface.py (prefix with ✗ Error:, clear messages)
- [X] T028 Add success message formatting to src/cli/interface.py (prefix with ✓, include relevant details)
- [X] T029 Manual testing per quickstart.md checklist (21 test cases covering basic ops, errors, edge cases)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 for add/view functionality to test
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Depends on US1 for add/view functionality to test
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Depends on US1 for add/view functionality to test

**Note**: US2, US3, and US4 technically depend on US1 for testing purposes (need to add/view todos to test their functionality), but their service layer implementations are independent.

### Within Each User Story

- Service methods before CLI handlers (service provides functionality CLI uses)
- CLI handlers before main.py updates (handlers must exist before being called)
- All tasks within a story should complete before moving to next priority

### Parallel Opportunities

- **Setup tasks**: T001, T002, T003 can run in parallel (different files)
- **Foundational tasks**: T004 and T005 can run in parallel (different files)
- **User Story 1**: T006 and T007 can run in parallel (different methods in same file)
- **Once Foundational completes**: US2, US3, and US4 service implementations (T013, T016, T019) can run in parallel if team capacity allows

---

## Parallel Example: User Story 1

```bash
# After Foundational phase completes, launch these tasks together:
Task T006: "Implement add_todo method in src/services/todo_service.py"
Task T007: "Implement get_all_todos method in src/services/todo_service.py"

# These are marked [P] because they're different methods in the same file
# and can be implemented independently
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T005) - CRITICAL blocking phase
3. Complete Phase 3: User Story 1 (T006-T012)
4. **STOP and VALIDATE**: Test User Story 1 independently using quickstart.md
5. Deploy/demo if ready - you now have a working todo app!

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T006-T012) → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 (T013-T015) → Test independently → Deploy/Demo
4. Add User Story 3 (T016-T018) → Test independently → Deploy/Demo
5. Add User Story 4 (T019-T021) → Test independently → Deploy/Demo
6. Add Polish (T022-T029) → Final testing → Production release
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T005)
2. Once Foundational is done:
   - Developer A: User Story 1 (T006-T012) - MUST complete first for others to test
   - After US1 complete:
     - Developer A: User Story 2 (T013-T015)
     - Developer B: User Story 3 (T016-T018)
     - Developer C: User Story 4 (T019-T021)
3. Stories complete and integrate independently
4. Team collaborates on Polish phase (T022-T029)

---

## Task Summary

**Total Tasks**: 29

**By Phase**:
- Setup: 3 tasks
- Foundational: 2 tasks (BLOCKING)
- User Story 1 (P1): 7 tasks (MVP)
- User Story 2 (P2): 3 tasks
- User Story 3 (P3): 3 tasks
- User Story 4 (P4): 3 tasks
- Polish: 8 tasks

**By User Story**:
- US1 (Add and View): 7 tasks
- US2 (Mark Complete): 3 tasks
- US3 (Update): 3 tasks
- US4 (Delete): 3 tasks
- Infrastructure: 5 tasks (Setup + Foundational)
- Cross-cutting: 8 tasks (Polish)

**Parallel Opportunities**: 4 tasks marked [P] can run in parallel within their phases

**MVP Scope**: Phases 1-3 (12 tasks) deliver a working todo app with add and view functionality

---

## Notes

- [P] tasks = different files or independent methods, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Manual testing per quickstart.md is the primary validation approach
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Validation Checklist

After completing all tasks, verify:

- [ ] All 5 core operations work (add, view, update, delete, mark complete)
- [ ] Menu displays correctly with 6 options
- [ ] Invalid inputs show clear error messages
- [ ] Empty descriptions are rejected
- [ ] Non-existent IDs are handled gracefully
- [ ] Completion status displays correctly ([ ] vs [✓])
- [ ] IDs are sequential and never reused
- [ ] Exit option terminates cleanly
- [ ] Application handles 100+ todos without performance issues
- [ ] All acceptance scenarios from spec.md pass
- [ ] Manual testing checklist from quickstart.md complete (21 tests)

---

## References

- Feature Specification: `specs/001-console-todo-app/spec.md`
- Implementation Plan: `specs/001-console-todo-app/plan.md`
- Data Model: `specs/001-console-todo-app/data-model.md`
- CLI Interface Contract: `specs/001-console-todo-app/contracts/cli-interface.md`
- Quickstart Guide: `specs/001-console-todo-app/quickstart.md`
- Research Document: `specs/001-console-todo-app/research.md`
