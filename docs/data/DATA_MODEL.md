# ATHENA Canonical Data Model

> **The single source of truth for all business entities in ATHENA**

---

| Property | Value |
|----------|-------|
| Document | DATA_MODEL.md |
| Document ID | ATH-DATA-001 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | Data Architecture |
| Depends On | ATHENA_SYSTEM_ARCHITECTURE.md |
| Related Documents | ATHENA_SERVICE_CATALOG.md, ENTITY_RELATIONSHIP.md |

---

# Purpose

The Canonical Data Model (CDM) defines the core business entities of ATHENA.

It provides a consistent representation of business concepts across:

- Services
- APIs
- Database
- AI Agents
- Event Bus
- Reports
- Analytics

Every entity shall have one and only one owning service.

---

# Design Principles

ATHENA follows Domain-Driven Design (DDD).

Rules:

- Business entities are defined before database tables.
- Every entity has a single owner.
- Every entity has a lifecycle.
- Services communicate through entities and events.
- No duplicated ownership.

---

# Domain Overview

```text
Market
   │
   ▼
Sector
   │
   ▼
Stock
   │
   ▼
Feature
   │
   ▼
Setup
   │
   ▼
Probability Assessment
   │
   ▼
Investment Case
   │
   ▼
Decision
   │
   ▼
Trade
   │
   ▼
Outcome
   │
   ▼
Lesson
   │
   ▼
Knowledge
   │
   ▼
Learning
```

---

# Entity Standards

Every entity must include the following metadata.

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier |
| created_at | Timestamp | Creation time |
| updated_at | Timestamp | Last modification |
| created_by | UUID | User or Service |
| version | Integer | Entity version |
| status | Enum | Current lifecycle state |
| tags | Array | Optional labels |

---

# Core Business Entities

---

## MarketState

### Owner

Market Intelligence Service

### Purpose

Represents the overall condition of the market.

### Attributes

- Market Regime
- Market Health Score
- Breadth
- Volatility
- Trend
- FII Activity
- DII Activity
- Trading Session

Lifecycle

```
Open

↓

Updated

↓

Closed

↓

Archived
```

---

## SectorState

### Owner

Market Intelligence Service

Represents the health of a sector.

Attributes

- Sector Name
- Relative Strength
- Momentum
- Trend
- Ranking

---

## Stock

### Owner

Scanner Intelligence Service

Represents a tradable security.

Attributes

- Symbol
- Company Name
- Exchange
- Industry
- Sector
- Market Cap

---

## Indicator

### Owner

Feature Engineering

Represents calculated indicators.

Examples

- EMA
- RSI
- MACD
- ATR
- ADX
- VWAP
- Bollinger Bands

Indicators are immutable once calculated.

---

## Feature

### Owner

Feature Engineering

Represents engineered numerical features.

Examples

- Relative Strength
- Gap Percentage
- Volume Spike
- Breakout Score
- Momentum Score

Stored in the Feature Store.

---

## Setup

### Owner

Setup Intelligence Service

Represents a standardized trading opportunity.

Examples

- EMA Pullback
- Breakout
- Trend Continuation
- Mean Reversion
- Dividend Accumulation

Lifecycle

```
Detected

↓

Validated

↓

Ranked

↓

Expired
```

---

## ProbabilityAssessment

### Owner

Probabilistic Intelligence Service

Represents probability estimation.

Attributes

- Success Probability
- Confidence
- Historical Matches
- Expected Return
- Expected Drawdown
- Expected Holding Period

---

## InvestmentCase

### Owner

Investment Decision Service

Represents a complete investment proposal.

Contains

- Setup
- Probability
- Evidence
- Counterarguments
- Recommendation
- Committee Notes

---

## ValidationReport

### Owner

Validation Intelligence Service

Represents independent validation.

Checks

- Liquidity
- Correlation
- Earnings Calendar
- Risk Budget
- Exposure
- Market Conditions

Status

- Approved
- Rejected
- Needs Review

---

## RiskProfile

### Owner

Risk Intelligence Service

Represents investment risk.

Attributes

- Position Size
- Stop Loss
- Risk Score
- Portfolio Heat
- Drawdown
- Exposure

---

## Portfolio

### Owner

Portfolio Intelligence Service

Represents a collection of positions.

Types

- Swing
- Positional
- Dividend
- Watchlist

---

## Position

### Owner

Portfolio Intelligence Service

Represents one investment.

Attributes

- Entry
- Exit
- Quantity
- Average Cost
- Unrealized P/L
- Realized P/L

---

## Trade

### Owner

Portfolio Intelligence Service

Represents an executed transaction.

Lifecycle

```
Created

↓

Executed

↓

Closed

↓

Reviewed
```

---

## Decision

### Owner

Knowledge Intelligence Service

Represents the reasoning behind an investment.

Contains

- Evidence
- Probability
- Committee Votes
- Decision Score
- Final Verdict

---

## Lesson

### Owner

Knowledge Intelligence Service

Represents post-trade learning.

Examples

- Successful Pattern
- Mistake
- Improvement
- Observation

---

## Knowledge

### Owner

Knowledge Intelligence Service

Represents structured institutional memory.

Sources

- Decisions
- Lessons
- Research
- Strategies

---

## Learning

### Owner

Learning Intelligence Service

Represents improvements generated by ATHENA.

Examples

- Updated Probability
- Better Calibration
- Strategy Suggestions
- Model Improvements

---

## Strategy

### Owner

Strategy Lab

Represents an investment methodology.

Examples

- Swing Strategy
- Dividend Strategy
- Breakout Strategy

---

## Experiment

### Owner

Strategy Lab

Represents research.

Examples

- Backtest
- Walk Forward
- Monte Carlo
- Paper Trading

---

## Report

### Owner

Reporting Service

Represents generated reports.

Types

- Daily
- Weekly
- Monthly
- Quarterly
- Research
- Portfolio

---

## UserProfile

### Owner

Platform Services

Represents system users.

Roles

- Founder
- Admin
- Trader
- Analyst
- Researcher

---

# Entity Ownership Matrix

| Entity | Owner |
|---------|-------|
| MarketState | Market Intelligence |
| SectorState | Market Intelligence |
| Stock | Scanner Intelligence |
| Indicator | Feature Engineering |
| Feature | Feature Engineering |
| Setup | Setup Intelligence |
| ProbabilityAssessment | Probabilistic Intelligence |
| InvestmentCase | Investment Decision |
| ValidationReport | Validation Intelligence |
| RiskProfile | Risk Intelligence |
| Portfolio | Portfolio Intelligence |
| Position | Portfolio Intelligence |
| Trade | Portfolio Intelligence |
| Decision | Knowledge Intelligence |
| Lesson | Knowledge Intelligence |
| Knowledge | Knowledge Intelligence |
| Learning | Learning Intelligence |
| Strategy | Strategy Lab |
| Experiment | Strategy Lab |
| Report | Reporting |
| UserProfile | Platform Services |

---

# Entity Lifecycle

```text
MarketState
      │
      ▼
SectorState
      │
      ▼
Stock
      │
      ▼
Feature
      │
      ▼
Setup
      │
      ▼
Probability Assessment
      │
      ▼
Investment Case
      │
      ▼
Validation Report
      │
      ▼
Decision
      │
      ▼
Trade
      │
      ▼
Lesson
      │
      ▼
Knowledge
      │
      ▼
Learning
```

---

# Data Ownership Rules

Every entity:

- Has exactly one owning service.
- Cannot be modified by another service.
- Can be read by other services through APIs or events.
- Must publish lifecycle events.
- Must support versioning.

---

# Versioning

ATHENA follows optimistic versioning.

Rules:

- Every update increments `version`.
- Historical versions are retained for audit.
- AI models use immutable historical snapshots.

---

# Retention Policy

| Entity | Retention |
|---------|-----------|
| MarketState | 10 Years |
| Trade | Permanent |
| Decision | Permanent |
| Lesson | Permanent |
| Knowledge | Permanent |
| Reports | 10 Years |
| Audit Logs | Permanent |

---

# Future Extensions

The Canonical Data Model is designed to support future domains without structural redesign.

Potential extensions include:

- Options
- Futures
- ETFs
- Mutual Funds
- International Markets
- Enterprise Decision Support

---

# References

- ATHENA_ARCHITECTURE_HANDBOOK.md
- ATHENA_SYSTEM_ARCHITECTURE.md
- ATHENA_SERVICE_CATALOG.md
- ENTITY_RELATIONSHIP.md
- DATA_DICTIONARY.md

---

**End of Document**
