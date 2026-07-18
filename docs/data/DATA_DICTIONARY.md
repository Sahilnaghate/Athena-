# ATHENA Data Dictionary

> **The authoritative definition of every business entity, attribute, and data type used within ATHENA.**

---

| Property | Value |
|----------|-------|
| Document | DATA_DICTIONARY.md |
| Document ID | ATH-DATA-003 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | Data Architecture |

---

# Purpose

The Data Dictionary standardizes every entity attribute across ATHENA.

It ensures:

- Consistent naming
- Standard data types
- API consistency
- Database consistency
- AI prompt consistency

---

# Naming Standards

## Entity

PascalCase

Example

```
InvestmentCase
```

---

## Attributes

snake_case

```
market_regime

entry_price

holding_period
```

---

## IDs

UUID

```
id

user_id

portfolio_id

setup_id
```

---

## Date Fields

UTC Timestamp

```
created_at

updated_at

executed_at
```

---

# Common Metadata

Every entity contains:

| Field | Type | Required | Description |
|------|------|----------|-------------|
| id | UUID | Yes | Primary Identifier |
| created_at | TIMESTAMP | Yes | Creation Time |
| updated_at | TIMESTAMP | Yes | Last Update |
| version | INTEGER | Yes | Entity Version |
| status | ENUM | Yes | Lifecycle Status |
| created_by | UUID | Yes | User/Service |
| tags | JSON | No | Labels |

---

# Entity Definitions

---

# MarketState

| Attribute | Type | Description |
|------------|------|-------------|
| market_regime | ENUM | Bull/Bear/Sideways |
| market_health_score | DECIMAL | 0-100 |
| volatility_index | DECIMAL | VIX |
| market_breadth | DECIMAL | Breadth Ratio |
| fii_activity | DECIMAL | Net Buy/Sell |
| dii_activity | DECIMAL | Net Buy/Sell |
| session | ENUM | Pre/Open/Post |

---

# SectorState

| Attribute | Type |
|------------|------|
| sector_name | VARCHAR |
| ranking | INTEGER |
| momentum_score | DECIMAL |
| relative_strength | DECIMAL |
| trend | ENUM |

---

# Stock

| Attribute | Type |
|------------|------|
| symbol | VARCHAR |
| company_name | VARCHAR |
| exchange | VARCHAR |
| sector | VARCHAR |
| industry | VARCHAR |
| market_cap | DECIMAL |

---

# Indicator

| Attribute | Type |
|------------|------|
| indicator_name | VARCHAR |
| indicator_value | DECIMAL |
| timeframe | ENUM |
| calculation_time | TIMESTAMP |

---

# Feature

| Attribute | Type |
|------------|------|
| feature_name | VARCHAR |
| feature_value | DECIMAL |
| feature_version | INTEGER |
| source | VARCHAR |

---

# Setup

| Attribute | Type |
|------------|------|
| setup_name | VARCHAR |
| setup_type | ENUM |
| entry_price | DECIMAL |
| stop_loss | DECIMAL |
| target_price | DECIMAL |
| holding_period | INTEGER |
| confidence | DECIMAL |

---

# ProbabilityAssessment

| Attribute | Type |
|------------|------|
| probability | DECIMAL |
| confidence | DECIMAL |
| expected_return | DECIMAL |
| expected_drawdown | DECIMAL |
| historical_matches | INTEGER |

---

# InvestmentCase

| Attribute | Type |
|------------|------|
| recommendation | ENUM |
| decision_score | DECIMAL |
| evidence_score | DECIMAL |
| probability_score | DECIMAL |
| committee_summary | TEXT |

---

# ValidationReport

| Attribute | Type |
|------------|------|
| liquidity_check | BOOLEAN |
| earnings_check | BOOLEAN |
| exposure_check | BOOLEAN |
| correlation_check | BOOLEAN |
| validation_status | ENUM |

---

# RiskProfile

| Attribute | Type |
|------------|------|
| risk_score | DECIMAL |
| position_size | DECIMAL |
| max_loss | DECIMAL |
| portfolio_heat | DECIMAL |
| stop_loss | DECIMAL |

---

# Portfolio

| Attribute | Type |
|------------|------|
| portfolio_name | VARCHAR |
| portfolio_type | ENUM |
| total_value | DECIMAL |
| cash_balance | DECIMAL |
| total_return | DECIMAL |

---

# Position

| Attribute | Type |
|------------|------|
| quantity | DECIMAL |
| average_price | DECIMAL |
| current_price | DECIMAL |
| unrealized_pl | DECIMAL |
| realized_pl | DECIMAL |

---

# Trade

| Attribute | Type |
|------------|------|
| trade_type | ENUM |
| entry_time | TIMESTAMP |
| exit_time | TIMESTAMP |
| pnl | DECIMAL |
| trade_status | ENUM |

---

# Lesson

| Attribute | Type |
|------------|------|
| lesson_type | ENUM |
| lesson_summary | TEXT |
| recommendation | TEXT |

---

# Knowledge

| Attribute | Type |
|------------|------|
| knowledge_title | VARCHAR |
| knowledge_type | ENUM |
| source | VARCHAR |
| confidence | DECIMAL |

---

# Learning

| Attribute | Type |
|------------|------|
| learning_type | ENUM |
| improvement | TEXT |
| model_version | INTEGER |

---

# Strategy

| Attribute | Type |
|------------|------|
| strategy_name | VARCHAR |
| strategy_type | ENUM |
| win_rate | DECIMAL |
| average_return | DECIMAL |

---

# Experiment

| Attribute | Type |
|------------|------|
| experiment_name | VARCHAR |
| experiment_type | ENUM |
| result | ENUM |
| notes | TEXT |

---

# Report

| Attribute | Type |
|------------|------|
| report_name | VARCHAR |
| report_type | ENUM |
| generated_at | TIMESTAMP |
| report_status | ENUM |

---

# UserProfile

| Attribute | Type |
|------------|------|
| first_name | VARCHAR |
| last_name | VARCHAR |
| email | VARCHAR |
| role | ENUM |
| timezone | VARCHAR |

---

# Enumerations

## MarketRegime

- Bull
- Bear
- Sideways

---

## Recommendation

- BUY
- SELL
- HOLD
- WATCH
- EXIT
- NO_TRADE

---

## PortfolioType

- Swing
- Positional
- Dividend

---

## TradeStatus

- Pending
- Open
- Closed
- Cancelled

---

# Data Quality Rules

- UUID for all identifiers.
- UTC timestamps.
- Immutable IDs.
- Enum validation.
- Decimal precision for prices.
- No duplicate business keys.

---

# References

- DATA_MODEL.md
- ENTITY_RELATIONSHIP.md
- FEATURE_STORE.md
- ATHENA_SYSTEM_ARCHITECTURE.md

---

**End of Document**
