# ATHENA Service Catalog

> **"Every service has one responsibility. Every responsibility has one owner."**

---

| Property | Value |
|----------|-------|
| Document | ATHENA_SERVICE_CATALOG.md |
| Document ID | ATH-ARC-001 |
| Version | 1.0.0 |
| Status | Draft |
| Classification | System Architecture |
| Owner | ATHENA Labs |
| Project | ATHENA |
| Product | TradePilot AI |

---

# Purpose

The ATHENA Service Catalog defines every service in the platform.

For each service it specifies:

- Purpose
- Responsibilities
- Inputs
- Outputs
- Data Ownership
- APIs
- Events
- Dependencies
- Service Level Expectations

This document is the primary architectural reference for backend development.

---

# Architecture Overview

```
                         User Interface

                               │

                               ▼

                     API Gateway / Backend

                               │

────────────────────────────────────────────────────────────

               ATHENA Decision Intelligence Platform

────────────────────────────────────────────────────────────

Market Intelligence Service

↓

Scanner Intelligence Service

↓

Setup Intelligence Service

↓

Probability Intelligence Service

↓

Investment Committee Service

↓

Investment Decision Service

↓

Validation Intelligence Service

↓

Risk Intelligence Service

↓

Portfolio Intelligence Service

↓

Knowledge Intelligence Service

↓

Learning Intelligence Service

↓

Strategy Lab Service

↓

Reporting Service

────────────────────────────────────────────────────────────

                Shared AI Coach Service

────────────────────────────────────────────────────────────

Data Layer

Infrastructure

Monitoring

Notifications

Authentication
```

---

# Service Dependency Graph

```
Market Intelligence
        │
        ▼
Scanner Intelligence
        │
        ▼
Setup Intelligence
        │
        ▼
Probability Intelligence
        │
        ▼
Investment Committee
        │
        ▼
Investment Decision
        │
        ▼
Validation Intelligence
        │
        ▼
Risk Intelligence
        │
        ▼
Portfolio Intelligence
        │
        ▼
Knowledge Intelligence
        │
        ▼
Learning Intelligence
        │
        ▼
Strategy Lab
        │
        ▼
Reporting
```

---

# Service Catalog

---

# SERVICE-001

## Market Intelligence Service

### Purpose

Understand the current market environment.

### Responsibilities

- Detect Market Regime
- Calculate Market Health
- Sector Rotation
- Breadth Analysis
- Volatility
- FII/DII Analysis
- Global Market Summary
- Economic Calendar

### Inputs

- NSE Data
- BSE Data
- VIX
- Global Markets
- Calendar

### Outputs

- Market Regime
- Market Health Score
- Trading Environment
- Sector Ranking

### Data Owner

Market Database

### Publishes Events

MarketRegimeChanged

MarketHealthUpdated

SectorRankingUpdated

---

# SERVICE-002

## Scanner Intelligence Service

### Purpose

Identify trading setups.

### Responsibilities

- Long Scanner
- Short Scanner
- Dividend Scanner
- Breakout Scanner
- Pullback Scanner
- Watchlist Scanner

### Inputs

- Market Intelligence
- Price Data
- Indicators

### Outputs

- Setup Candidates

### Publishes

SetupDetected

ScannerCompleted

---

# SERVICE-003

## Setup Intelligence Service

### Purpose

Convert scanner output into standardized ATHENA setups.

Examples

- EMA Pullback
- Breakout
- Trend Continuation
- Mean Reversion
- Dividend Accumulation

### Outputs

Setup Objects

---

# SERVICE-004

## Probability Intelligence Service

### Purpose

Estimate historical probability.

### Responsibilities

- Historical Similarity
- Market Genome
- Trade DNA
- Decision DNA
- Bayesian Updates
- Confidence Calibration

### Outputs

- Probability
- Confidence
- Similar Cases

---

# SERVICE-005

## Investment Committee Service

### Purpose

Coordinate specialist agents.

Committee Members

- Market Analyst
- Technical Analyst
- Probability Expert
- Risk Manager
- Portfolio Manager
- Behaviour Coach
- Research Analyst

### Output

Committee Recommendation

---

# SERVICE-006

## Investment Decision Service

### Purpose

Produce final investment recommendation.

Possible Outputs

- BUY
- SHORT
- HOLD
- WAIT
- EXIT
- REDUCE
- NO TRADE

Produces

Investment Case File

---

# SERVICE-007

## Validation Intelligence Service

### Purpose

Validate recommendations before approval.

Checks

- Liquidity
- Earnings
- Correlation
- Portfolio
- Calendar
- Risk
- Exposure

Output

Approved

Rejected

Needs Review

---

# SERVICE-008

## Risk Intelligence Service

### Purpose

Protect capital.

Responsibilities

- Position Size
- Portfolio Heat
- Drawdown
- Exposure
- Risk Budget

Outputs

Risk Report

---

# SERVICE-009

## Portfolio Intelligence Service

### Purpose

Manage investments.

Responsibilities

- Holdings
- Allocation
- Performance
- Dividend Portfolio
- Trading Portfolio

---

# SERVICE-010

## Knowledge Intelligence Service

### Purpose

Capture institutional knowledge.

Responsibilities

- Decision Replay
- Case Files
- Decision Journal
- Trade Journal
- Lessons Learned
- Knowledge Graph

---

# SERVICE-011

## Learning Intelligence Service

### Purpose

Improve ATHENA.

Responsibilities

- Learn from completed trades
- Identify recurring mistakes
- Improve confidence calibration
- Suggest strategy improvements
- Generate research

Outputs

Learning Reports

---

# SERVICE-012

## Strategy Lab Service

### Purpose

Research.

Responsibilities

- Backtesting
- Walk Forward
- Experiments
- A/B Tests
- Strategy Validation

---

# SERVICE-013

## Reporting Service

### Purpose

Generate reports.

Reports

- Daily
- Weekly
- Monthly
- Quarterly
- Research
- Portfolio
- Decision
- Probability

---

# SERVICE-014

## AI Coach Service

### Purpose

Assist the user.

Capabilities

- Explain
- Compare
- Review
- Teach
- Challenge
- Recommend
- Summarize

Unlike other services,

AI Coach has read access to every service.

---

# Shared Infrastructure Services

Authentication Service

Notification Service

Logging Service

Monitoring Service

Configuration Service

Audit Service

Feature Flag Service

Scheduler Service

Cache Service

File Storage Service

---

# Service Ownership Matrix

| Service | Owner |
|----------|--------|
| Market Intelligence | Market Team |
| Scanner | Quant Team |
| Setup | Quant Team |
| Probability | Research Team |
| Investment Committee | AI Team |
| Decision | Decision Team |
| Validation | Risk Team |
| Risk | Risk Team |
| Portfolio | Portfolio Team |
| Knowledge | Research Team |
| Learning | AI Team |
| Strategy Lab | Research Team |
| Reporting | Platform Team |

---

# Service Principles

Every service shall:

- Have one responsibility.
- Own its own data.
- Publish events.
- Expose APIs.
- Be independently testable.
- Be independently deployable.
- Be independently observable.

No service should directly manipulate another service's data.

---

# Closing Statement

ATHENA is built as a collection of specialized intelligence services working together through clearly defined interfaces.

This architecture ensures:

- Scalability
- Maintainability
- Testability
- Explainability
- Future SaaS readiness

Every future feature must belong to exactly one service.

If ownership is unclear,

the architecture should be reconsidered before implementation.
