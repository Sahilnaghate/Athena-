# AGENTS.md

# ATHENA AI Development Operating Manual

> **This document defines how AI coding agents must behave while contributing to the ATHENA codebase.**

---

# Project

ATHENA

Evidence-Based Decision Intelligence Operating System (DIOS)

---

# Mission

ATHENA is **not** a trading bot.

ATHENA is an enterprise platform that improves investment decision quality using:

- Evidence
- Probability
- Risk Management
- Explainability
- Continuous Learning

Every implementation decision must support this mission.

---

# AI Agent Responsibilities

AI coding agents are responsible for:

- Writing production-quality code
- Following documented architecture
- Maintaining consistency
- Writing tests
- Updating documentation
- Respecting service boundaries

AI agents are **not** responsible for changing business requirements or architecture.

---

# Engineering Principles

Always follow:

1. Architecture before code
2. Documentation before implementation
3. Test before merge
4. Simplicity over cleverness
5. Readability over brevity
6. Security by default
7. Explainability by design

---

# Repository Structure

Never modify this structure without an approved ADR.

```
apps/
packages/
database/
docs/
tests/
infrastructure/
.github/
```

---

# Source of Truth

If documents disagree, use this priority.

1. ADRs
2. ATHENA_ARCHITECTURE_HANDBOOK.md
3. ATHENA_SYSTEM_ARCHITECTURE.md
4. ATHENA_SERVICE_CATALOG.md
5. Database Schema
6. API Specifications
7. Sprint Documents

Never invent architecture.

---

# Service Rules

Each service owns:

- Its business logic
- Its database schema
- Its API
- Its events

Never:

- Write directly into another service's schema
- Duplicate business logic
- Bypass service APIs

---

# Database Rules

Always use

- UUID v7
- Alembic migrations
- SQLAlchemy models
- Repository pattern

Never write raw SQL in business logic unless explicitly justified.

---

# API Rules

Use:

- REST
- OpenAPI 3.1
- Versioned endpoints

Every endpoint must include:

- Validation
- Authentication
- Authorization
- Documentation
- Tests

---

# AI Rules

ATHENA uses a multi-agent architecture.

Never replace it with a single AI agent.

Specialist agents include:

- Market Analyst
- Technical Analyst
- Probability Expert
- Risk Manager
- Portfolio Manager
- Behaviour Coach
- Research Analyst
- Knowledge Advisor
- Learning Advisor

The AI Orchestrator coordinates these agents.

---

# Code Generation Rules

Generate:

- Small commits
- Small pull requests
- Modular code
- Typed code
- Tested code

Avoid generating thousands of lines at once.

---

# Naming Standards

Files

```
kebab-case
```

Classes

```
PascalCase
```

Variables

```
camelCase
```

Constants

```
UPPER_SNAKE_CASE
```

Database

```
snake_case
```

---

# Testing Requirements

Every feature requires:

- Unit tests
- Integration tests
- API tests

Core financial modules additionally require:

- Boundary tests
- Regression tests
- Scenario tests

---

# Security Requirements

Never:

- Hardcode secrets
- Disable authentication
- Disable authorization
- Trust user input

Always:

- Validate
- Sanitize
- Escape
- Log securely

---

# Logging

Use structured logging only.

Never use:

```
console.log()
```

Always include:

- Request ID
- Correlation ID
- User ID (if available)
- Service name
- Execution time

---

# Documentation

Whenever code changes:

Update documentation if:

- API changes
- Database changes
- Events change
- Architecture changes

---

# Pull Requests

Every PR must include:

- Summary
- Reason
- Tests
- Risks
- Documentation updates

---

# Things AI Must Never Do

Do not:

- Change architecture
- Rename services
- Modify schemas owned by another service
- Skip tests
- Remove logging
- Ignore lint errors
- Ignore type errors

---

# Decision Making

If uncertain:

STOP.

Leave a TODO.

Request clarification.

Never invent missing requirements.

---

# Current Sprint

Sprint 001

Scope:

- Platform Skeleton
- Docker
- PostgreSQL
- Redis
- FastAPI
- Next.js
- Authentication
- Market Service
- Scanner Service
- Setup Service
- Probability Service

Ignore future sprint features.

---

# Quality Gates

Code is complete only if:

- Builds successfully
- Lint passes
- Tests pass
- Documentation updated
- API documented
- Migration created
- CI/CD passes

---

# AI Collaboration

Different AI tools have different roles.

| Tool | Primary Responsibility |
|------|-------------------------|
| ChatGPT | CTO, Architecture, Product |
| Codex | Software Implementation |
| Claude Code | Code Review, Architecture Review |
| GitHub Copilot | Developer Assistance |

All AI-generated code must follow the same standards.

---

# Long-Term Goal

Build software that remains understandable,
maintainable,
and extensible for at least ten years.

Prefer correctness over speed.

Prefer clarity over cleverness.

Prefer maintainability over premature optimization.

---

# References

Read before making changes:

- CODEX.md
- ATHENA_ARCHITECTURE_HANDBOOK.md
- ATHENA_SYSTEM_ARCHITECTURE.md
- ATHENA_SERVICE_CATALOG.md
- ENGINEERING_STANDARDS.md
- CODING_STANDARDS.md
- TESTING_STRATEGY.md
- DATABASE_ARCHITECTURE.md
- AI_AGENT_ARCHITECTURE.md
- AI_ORCHESTRATION_ENGINE.md

---

**End of Document**
