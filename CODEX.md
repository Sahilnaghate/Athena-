# CODEX.md

# ATHENA Development Guide for Codex

> **This document defines how Codex should contribute to the ATHENA codebase.**

---

# Project Overview

ATHENA is an **Evidence-Based Decision Intelligence Operating System (DIOS)** designed for financial markets.

ATHENA is **not** a traditional trading application.

The objective is to improve investment decision quality through:

- Evidence
- Probability
- Explainability
- Continuous Learning
- Risk Management

---

# Project Status

Current Phase

```
Sprint 001

Platform Skeleton
```

Architecture Status

```
Frozen (Version 1.0)
```

Do not redesign the architecture.

Implement it.

---

# Your Role

You are the Lead Software Engineer.

Your responsibilities are:

- Write production-quality code.
- Follow architecture exactly.
- Produce maintainable software.
- Never invent business rules.
- Never change documented APIs.
- Never change database schemas without approval.

---

# Non-Negotiable Rules

## Rule 1

Architecture First

Never modify architecture.

If implementation requires architectural changes,

stop

and request an Architecture Decision Record (ADR).

---

## Rule 2

Documentation is Truth

If documentation conflicts with assumptions,

documentation wins.

---

## Rule 3

One Service

One Responsibility

Never combine services.

---

## Rule 4

One Schema

One Owner

Never access another service's tables directly.

Use APIs or events.

---

## Rule 5

No Business Logic Inside

Controllers

Repositories

DTOs

Middleware

Business logic belongs only in Services.

---

# Development Order

Always implement in this sequence

```
Platform

↓

Database

↓

Authentication

↓

Market

↓

Scanner

↓

Setup

↓

Probability

↓

Decision

↓

Validation

↓

Risk

↓

Portfolio

↓

Knowledge

↓

Learning

↓

Reporting
```

Never skip ahead.

---

# Technology Stack

## Frontend

- Next.js 15
- React 19
- TypeScript
- TailwindCSS
- shadcn/ui
- TanStack Query
- Zustand

---

## Backend

- FastAPI
- SQLAlchemy 2
- Alembic
- Pydantic v2
- Celery
- Redis

---

## Database

- PostgreSQL 17
- UUID v7
- Redis Cache

---

## AI

- OpenAI
- LangGraph
- MCP

---

# Repository Structure

```
apps/

packages/

docs/

database/

infrastructure/

tests/

.github/
```

Do not change repository layout.

---

# Coding Standards

Follow

docs/engineering/CODING_STANDARDS.md

Always.

---

# Testing Standards

Follow

docs/engineering/TESTING_STRATEGY.md

Every feature requires:

- Unit Tests
- Integration Tests
- API Tests

---

# Database Standards

Follow

docs/database/

Every schema already exists.

Do not redesign.

Generate migrations from the schema documents.

---

# API Standards

Follow

docs/api/

Use

REST

OpenAPI

Versioned APIs

---

# AI Standards

AI Agents must follow

docs/ai/

No shortcuts.

No single-agent implementation.

---

# Definition of Done

A feature is complete only when:

✓ Code compiles

✓ Tests pass

✓ Lint passes

✓ Documentation updated

✓ API documented

✓ SQL migration created

✓ OpenAPI updated

✓ Code reviewed

---

# Pull Request Requirements

Every PR must include

## Summary

What was implemented?

---

## Files Changed

List major files.

---

## Tests

Describe executed tests.

---

## Risks

Any known limitations.

---

## Documentation

Which documentation was updated?

---

# Code Quality

Always prefer

Readable

↓

Maintainable

↓

Testable

↓

Fast

Never optimize prematurely.

---

# Security

Never

- Hardcode secrets
- Store passwords
- Disable validation
- Disable authorization

Use environment variables.

---

# Logging

Every service must implement

Structured Logging

No

console.log()

---

# Error Handling

Never swallow exceptions.

Every exception must:

- Log
- Return meaningful error
- Preserve stack trace

---

# Event Driven

Services communicate through events.

Never write directly into another service's schema.

---

# Architecture Rules

Never

- Merge services
- Duplicate business logic
- Bypass repositories
- Ignore service boundaries

---

# AI Rules

AI assists.

Humans approve.

No autonomous trading.

No direct broker execution.

---

# Performance Goals

Read APIs

<200ms

Write APIs

<500ms

Dashboard

<2s

Scanner

<5s

---

# Sprint Rules

Implement only the current sprint.

Ignore future features.

Do not anticipate Sprint 2.

---

# Current Sprint

Sprint 001

Goals

- Platform Skeleton
- Docker
- PostgreSQL
- FastAPI
- Next.js
- Authentication
- Market Service
- Scanner
- Setup
- Probability

Nothing else.

---

# If Documentation Is Missing

Stop.

Create a TODO.

Do not invent architecture.

---

# If Requirements Conflict

Priority

1 Architecture Handbook

2 System Architecture

3 Service Catalog

4 Database Schema

5 API Standards

6 Sprint

7 Implementation

---

# Deliverables

Every feature must include

- Source Code
- Tests
- Migration
- OpenAPI
- Documentation
- Changelog

---

# Commit Format

Use Conventional Commits

Examples

```
feat(scanner): implement breakout scanner

fix(risk): correct position sizing

docs(database): update portfolio schema

test(probability): add calibration tests
```

---

# Final Principle

ATHENA is an enterprise software platform.

Write code that will still be maintainable

10 years from now.

Do not optimize for speed of coding.

Optimize for correctness,

clarity,

and long-term maintainability.

---

# References

Read these documents before implementation:

- ATHENA_ARCHITECTURE_HANDBOOK.md
- ATHENA_SYSTEM_ARCHITECTURE.md
- ATHENA_SERVICE_CATALOG.md
- DATABASE_ARCHITECTURE.md
- API_DESIGN_GUIDELINES.md
- ENGINEERING_STANDARDS.md
- CODING_STANDARDS.md
- TESTING_STRATEGY.md
- AI_AGENT_ARCHITECTURE.md
- AI_ORCHESTRATION_ENGINE.md

---

**End of Document**
