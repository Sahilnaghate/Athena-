# ATHENA Coding Standards

> **The official coding standards for ATHENA**

---

| Property | Value |
|----------|-------|
| Document | CODING_STANDARDS.md |
| Document ID | ATH-ENG-002 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | Engineering Standards |
| Depends On | ENGINEERING_STANDARDS.md |

---

# Purpose

This document defines coding standards for every software component
within ATHENA.

These standards ensure the codebase remains:

- Readable
- Maintainable
- Testable
- Secure
- Consistent
- Production Ready

These rules apply equally to:

- Human Developers
- Codex
- Claude Code
- GitHub Copilot
- AI Code Generators

---

# Core Philosophy

Code is written once.

It is read hundreds of times.

Always optimize for readability.

---

# General Principles

1. Simplicity over cleverness
2. Explicit over implicit
3. Composition over inheritance
4. Small functions
5. Single Responsibility Principle
6. Fail fast
7. Prefer immutability
8. No duplicate logic

---

# Naming Standards

## Variables

camelCase

Good

```ts
marketHealthScore

entryPrice

expectedReturn
```

Bad

```ts
x

temp

abc

score1
```

---

## Constants

UPPER_SNAKE_CASE

```ts
MAX_POSITION_SIZE

DEFAULT_TIMEOUT

API_VERSION
```

---

## Functions

camelCase

Function names must describe actions.

Good

```ts
calculateRisk()

generateProbability()

validatePortfolio()

fetchMarketState()
```

Bad

```ts
calc()

process()

run()

execute()
```

---

## Classes

PascalCase

```ts
MarketService

ProbabilityEngine

PortfolioRepository

RiskCalculator
```

---

## Interfaces

Prefix with "I" is NOT required.

Good

```ts
MarketRepository

TradeService

PortfolioStore
```

---

## Files

kebab-case

Examples

```
market-service.ts

risk-calculator.ts

portfolio-controller.ts

decision-engine.ts
```

---

## Folders

Lowercase

```
services

repositories

controllers

models

events

tests
```

---

# Folder Structure

```
src/

    controllers/

    services/

    repositories/

    models/

    dto/

    events/

    middleware/

    utils/

    config/

    tests/
```

---

# Function Standards

Functions should:

- Have one responsibility
- Be deterministic
- Be testable
- Avoid side effects

Preferred size

```
10–40 lines
```

Maximum

```
80 lines
```

---

# Method Parameters

Avoid long parameter lists.

Bad

```ts
createTrade(
symbol,
price,
quantity,
stopLoss,
target,
strategy,
notes,
user
)
```

Prefer

```ts
createTrade(CreateTradeRequest)
```

---

# Return Values

Always return typed objects.

Avoid

```ts
return true
```

Prefer

```ts
return {
success: true,
tradeId
}
```

---

# Error Handling

Never

```ts
catch (e) {}
```

Always

- Log
- Wrap
- Re-throw if appropriate

Example

```ts
try {

}
catch(error){

logger.error(error)

throw new TradeExecutionError()

}
```

---

# Magic Numbers

Never

```ts
if(risk > 3)
```

Always

```ts
const MAX_RISK_SCORE = 3

if(risk > MAX_RISK_SCORE)
```

---

# Comments

Comments explain

WHY

not

WHAT

Bad

```ts
// Increment i

i++
```

Good

```ts
// Risk score must remain below
// regulatory threshold.
```

---

# Logging

Use structured logging.

Good

```ts
logger.info({

tradeId,

symbol,

executionTime

})
```

Never

```ts
console.log()
```

---

# Dependency Injection

Always inject dependencies.

Never instantiate inside services.

Bad

```ts
const repo = new TradeRepository()
```

Good

```ts
constructor(

private repo: TradeRepository

){}
```

---

# Configuration

Never hardcode

URLs

Secrets

Tokens

Credentials

Use environment variables.

---

# Validation

Validate

- Input
- Output
- Business Rules

Never trust client input.

---

# Asynchronous Code

Always use

async / await

Avoid nested promises.

---

# Database Access

All database access goes through repositories.

Never query the database directly from controllers.

Correct flow

```
Controller

↓

Service

↓

Repository

↓

Database
```

---

# Events

Services publish events.

Never call another service's database.

Correct

```
TradeCreated

↓

Event Bus

↓

Portfolio Service
```

---

# Testing

Every public method requires tests.

Minimum

- Happy path
- Validation
- Failure
- Edge cases

---

# Code Duplication

If logic appears twice,

extract it.

Follow the

DRY

principle.

---

# Security

Never

- Log passwords
- Log tokens
- Store secrets in source code
- Trust user input

Always

- Validate
- Escape
- Sanitize

---

# Documentation

Every public function must include:

- Purpose
- Parameters
- Returns
- Exceptions

Example

```ts
/**
 * Calculates recommended
 * position size.
 *
 * @param capital
 * @param riskPercentage
 *
 * @returns Position Size
 */
```

---

# Complexity Limits

Cyclomatic Complexity

Maximum

```
10
```

Function Length

Maximum

```
80 lines
```

File Length

Target

```
<500 lines
```

---

# Code Review Checklist

Every Pull Request must verify:

- Naming
- Tests
- Logging
- Security
- Error Handling
- Documentation
- Architecture Compliance

---

# AI Generated Code

AI-generated code must:

- Follow these standards
- Pass linting
- Pass tests
- Be reviewed
- Be understandable

AI code is not exempt from engineering standards.

---

# Definition of Done

Code is complete only if:

- Builds successfully
- Passes tests
- Follows naming standards
- Has documentation
- Has logging
- Has validation
- Meets architecture guidelines

---

# References

- ENGINEERING_STANDARDS.md
- ATHENA_ARCHITECTURE_HANDBOOK.md
- API_DESIGN_GUIDELINES.md
- TESTING_STRATEGY.md
- LOGGING_STANDARD.md

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | July 2026 | Initial Coding Standards |

---

**End of Document**
