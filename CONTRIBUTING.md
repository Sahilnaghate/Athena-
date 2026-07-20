# Contributing to ATHENA

Welcome to **ATHENA – Evidence-Based Decision Intelligence Operating System (DIOS)**.

Thank you for your interest in contributing.

This document explains the development workflow, coding standards, and contribution process for the ATHENA project.

---

# Development Philosophy

ATHENA is built around the following principles:

- Architecture First
- Documentation Driven Development
- Testable Software
- Maintainable Code
- Security by Default
- Explainability over Complexity

Every contribution should improve the long-term quality of the platform.

---

# Before You Start

Read the following documents before contributing:

- README.md
- PROJECT_RULES.md
- AGENTS.md
- CODEX.md
- docs/architecture/ATHENA_ARCHITECTURE_HANDBOOK.md
- docs/engineering/CODING_STANDARDS.md
- docs/sprints/SPRINT-001.md

---

# Development Workflow

Never work directly on `main`.

Use the following Git workflow.

```text
main
│
├── develop
│
├── feature/market-intelligence
├── feature/scanner-intelligence
├── feature/setup-intelligence
└── feature/probability-engine
```

### Create a Feature Branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/<feature-name>
```

Example:

```bash
git checkout -b feature/market-intelligence
```

---

# Commit Messages

Use **Conventional Commits**.

Examples:

```text
feat(market): implement market overview API

fix(scanner): correct breakout filtering

docs(api): update market endpoints

test(probability): add confidence score tests

refactor(portfolio): simplify repository layer
```

---

# Pull Request Process

Every Pull Request must include:

## Summary

What was implemented?

## Motivation

Why was the change required?

## Testing

Describe the tests executed.

## Documentation

List updated documentation.

## Risks

Mention any known limitations.

---

# Coding Standards

Follow:

- TypeScript Strict Mode
- Python Type Hints
- Repository Pattern
- Dependency Injection
- SOLID Principles

Business logic belongs only in the Service layer.

Never place business logic inside:

- Controllers
- Repositories
- DTOs
- Middleware

---

# Database Standards

Database changes must include:

- SQLAlchemy model
- Alembic migration
- Repository updates
- Documentation updates

Never modify another service's schema directly.

---

# API Standards

All APIs must:

- Be versioned (`/api/v1/...`)
- Be documented in OpenAPI
- Return consistent response models
- Validate all input
- Handle errors gracefully

---

# Testing Requirements

Every contribution requires:

- Unit Tests
- Integration Tests

Financial logic additionally requires:

- Edge-case tests
- Regression tests

---

# Documentation

Update documentation whenever you change:

- API
- Database
- Events
- Architecture
- Configuration

---

# Security

Never:

- Commit secrets
- Disable authentication
- Disable authorization
- Trust user input

Use environment variables for configuration.

---

# Code Review Checklist

Before requesting review:

- Code builds successfully
- Tests pass
- Lint passes
- Documentation updated
- No debugging code remains
- No commented-out code
- No unused imports

---

# Local Development

Start the platform:

```bash
docker compose up --build
```

Run tests:

```bash
pnpm test
```

Backend tests:

```bash
pytest
```

Lint:

```bash
pnpm lint
```

---

# Branch Protection

The `main` branch is protected.

Changes must be merged through Pull Requests after:

- CI passes
- Review is completed
- Documentation is updated

---

# Definition of Done

A feature is complete only when:

- Code implemented
- Tests passing
- Documentation updated
- API documented
- Migration created
- CI successful
- Review approved

---

# Need Help?

If requirements are unclear:

1. Review the project documentation.
2. Open a GitHub Discussion or Issue.
3. Do not invent missing requirements.

---

Thank you for helping build ATHENA.
