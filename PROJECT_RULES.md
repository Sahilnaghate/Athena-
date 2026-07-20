# PROJECT_RULES.md

# ATHENA Project Rules

> **Master Governance Document for the ATHENA Platform**

---

## Document Information

| Property | Value |
|----------|-------|
| Project | ATHENA |
| Full Name | ATHENA – Evidence-Based Decision Intelligence Operating System (DIOS) |
| Version | 2.0 |
| Status | Active |
| Owner | Dr. Sahil G. Naghate |
| Last Updated | July 2026 |

---

# 1. Purpose

This document defines the governance, engineering principles, development workflow, and project standards for ATHENA.

It is the **single source of truth** for how the project is planned, developed, reviewed, tested, and released.

All contributors, whether human or AI, must follow the rules defined in this document.

---

# 2. Vision

ATHENA aims to become the world's most trusted **Evidence-Based Decision Intelligence Platform** for financial markets.

Rather than predicting markets, ATHENA helps investors make disciplined, explainable, and data-driven investment decisions through structured evidence, probability, and continuous learning.

---

# 3. Mission

Our mission is to build software that enables better investment decisions by combining:

- Evidence
- Probability
- Explainability
- Risk Management
- Continuous Learning
- Artificial Intelligence

ATHENA is designed to support disciplined investing—not speculative or automated trading.

---

# 4. Core Principles

Every engineering and product decision should align with these principles.

## 4.1 Evidence First

Every recommendation must be supported by measurable evidence.

No recommendation should rely solely on AI-generated opinions.

---

## 4.2 Explainability

Every recommendation must be explainable.

Users should always understand:

- Why a recommendation exists
- Which factors contributed
- What assumptions were made
- What risks remain

---

## 4.3 Probability Over Prediction

ATHENA does not predict the future.

Instead, it estimates probabilities based on historical patterns, current market conditions, and available evidence.

---

## 4.4 Risk Before Return

Capital preservation takes priority over maximizing returns.

Every recommendation must include an assessment of risk.

---

## 4.5 Continuous Learning

Every completed investment decision becomes new knowledge.

ATHENA continuously improves through structured feedback and learning.

---

## 4.6 Enterprise Quality

ATHENA is developed as enterprise software.

Every contribution should prioritize:

- Reliability
- Maintainability
- Security
- Scalability
- Testability

---

# 5. Governance Model

ATHENA follows a structured governance model.

## Product Owner

Responsible for:

- Product vision
- Business priorities
- Feature approval

Current Owner:

**Dr. Sahil G. Naghate**

---

## CTO / Architecture

Responsible for:

- System architecture
- Engineering decisions
- Technical roadmap
- Code review
- Architecture governance

---

## AI Engineering

AI coding assistants may:

- Generate code
- Generate tests
- Improve documentation
- Suggest refactoring

AI coding assistants must **not**:

- Change architecture
- Invent business rules
- Modify governance
- Bypass documented standards

---

## Source of Truth

If documentation conflicts, use the following priority:

1. PROJECT_RULES.md
2. Architecture Decision Records (ADRs)
3. Architecture Handbook
4. Service Catalog
5. Database Documentation
6. API Documentation
7. Sprint Documents

---

# Guiding Principle

Every technical decision should support the long-term vision of ATHENA.

When multiple solutions are possible, choose the option that maximizes:

- Clarity
- Maintainability
- Correctness
- Long-term sustainability

---

**End of Part 1**
