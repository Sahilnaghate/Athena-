# GitHub Copilot Instructions

Welcome to ATHENA.

This repository follows strict architecture and engineering standards.

## Before Writing Code

Read:

- AGENTS.md
- CODEX.md
- docs/architecture/ATHENA_ARCHITECTURE_HANDBOOK.md
- docs/engineering/CODING_STANDARDS.md

## Architecture

ATHENA uses:

- Domain-Driven Design
- Service-Oriented Architecture
- Event-Driven Communication
- Repository Pattern
- Feature Store
- Knowledge Graph
- Multi-Agent AI

Do not introduce alternative architectures.

## Code Style

Follow:

- TypeScript strict mode
- Python type hints
- Small focused functions
- Repository pattern
- Dependency injection
- Structured logging

## Tests

Every feature should include:

- Unit Tests
- Integration Tests

Critical financial logic additionally requires:

- Edge-case tests
- Regression tests

## Security

Never:

- Hardcode credentials
- Skip authentication
- Trust client input

Always:

- Validate
- Sanitize
- Escape

## Documentation

Whenever changing:

- APIs
- Database
- Events
- Architecture

Update the corresponding documentation.

## Development Order

Current Sprint

Sprint 001

Only implement:

- Platform Skeleton
- Market Service
- Scanner Service
- Setup Service
- Probability Service

Ignore future sprint features unless instructed.

## Quality Gates

Code is acceptable only if:

- Builds successfully
- Lint passes
- Tests pass
- Documentation updated
- CI pipeline passes
