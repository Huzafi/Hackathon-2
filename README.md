# Phase I Console Todo App

**Version**: 1.0.0
**Status**: In Development
**Phase**: I - In-Memory Console Application

## Overview

A simple command-line todo application that stores tasks in memory. This is Phase I of a five-phase project that will evolve from console to full-stack to AI-powered to cloud-native deployment.

## Features

- ✅ Add new todos with text descriptions
- ✅ View all todos with completion status
- ✅ Update todo descriptions
- ✅ Delete todos
- ✅ Mark todos as complete
- ✅ In-memory storage (no persistence)
- ✅ Clean console interface

## Requirements

- Python 3.13 or higher
- UV package manager

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Hackathon-Phase-2

# Initialize UV environment (if not already done)
uv init

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
```

## Usage

```bash
# Run the application
python src/main.py
```

### Menu Options

1. **Add todo** - Create a new todo item
2. **View all todos** - Display all todos with their status
3. **Update todo** - Edit an existing todo's description
4. **Delete todo** - Remove a todo from the list
5. **Mark todo complete** - Mark a todo as completed
6. **Exit** - Close the application

## Project Structure

```
Hackathon-Phase-2/
├── src/
│   ├── models/
│   │   └── todo.py          # Todo data model
│   ├── services/
│   │   └── todo_service.py  # Business logic and CRUD operations
│   ├── cli/
│   │   └── interface.py     # Console interface and user interaction
│   └── main.py              # Application entry point
├── tests/
│   ├── integration/         # Integration tests (optional)
│   └── unit/                # Unit tests (optional)
├── specs/                   # Design documentation
├── pyproject.toml           # UV project configuration
└── README.md                # This file
```

## Design Principles

- **Simplicity First**: Clear, minimal, understandable logic
- **Correctness**: Predictable state handling for all operations
- **Modularity**: Code structured for reuse in later phases
- **No Persistence**: All data is in-memory only (Phase I constraint)

## Phase Roadmap

- **Phase I** (Current): In-memory Python console app
- **Phase II**: Full-stack web app (Next.js + FastAPI + Neon DB)
- **Phase III**: AI-powered todo chatbot (OpenAI + Agents SDK)
- **Phase IV**: Local Kubernetes deployment (Docker + Minikube)
- **Phase V**: Advanced cloud deployment (Kafka + Dapr + DOKS)

## Testing

Manual testing is the primary validation approach for Phase I. See `specs/001-console-todo-app/quickstart.md` for the complete testing checklist (21 test cases).

## Known Limitations (Phase I)

- No data persistence (todos lost when app closes)
- Single-user only
- No undo/redo functionality
- No search or filtering
- No categories or priorities
- Console interface only

These limitations are intentional for Phase I and will be addressed in later phases.

## Documentation

Complete design documentation is available in `specs/001-console-todo-app/`:
- `spec.md` - Feature specification
- `plan.md` - Implementation plan
- `data-model.md` - Data structures
- `contracts/cli-interface.md` - CLI interface specification
- `quickstart.md` - Testing guide
- `research.md` - Architecture decisions

## License

Generated via agentic workflow using Claude Code.

## Contributing

This is a demonstration project for agentic development. See the constitution at `.specify/memory/constitution.md` for development principles.

## 🎥 Hackathon 2 Phase II
[Phase II Repo Link](https://github.com/Huzafi/Hackathon-2-Phase-II)
