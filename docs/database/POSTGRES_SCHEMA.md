# ATHENA PostgreSQL Schema

> **Master PostgreSQL Schema Specification for ATHENA**

---

| Property | Value |
|----------|-------|
| Document | POSTGRES_SCHEMA.md |
| Document ID | ATH-DB-003 |
| Version | 1.0.0 |
| Status | Draft |
| Database | PostgreSQL 17+ |
| Owner | ATHENA Labs |

---

# Purpose

This document defines the PostgreSQL schema organization used by ATHENA.

It is the master reference for:

- Database schemas
- Tables
- Constraints
- Indexes
- Relationships
- Migrations

Detailed table definitions are maintained in the `/schemas` directory.

---

# Database Overview

ATHENA uses a **schema-per-domain** architecture.

Each business domain owns its own PostgreSQL schema.

No domain directly modifies another domain's tables.

Communication occurs through:

- APIs
- Domain Events

---

# Database Structure

```
PostgreSQL

├── market
├── scanner
├── setup
├── probability
├── decision
├── validation
├── risk
├── portfolio
├── knowledge
├── learning
├── reporting
├── auth
├── config
├── audit
```

---

# Schema Ownership

| PostgreSQL Schema | Service Owner |
|------------------|---------------|
| market | Market Intelligence |
| scanner | Scanner Intelligence |
| setup | Setup Intelligence |
| probability | Probability Service |
| decision | Decision Service |
| validation | Validation Service |
| risk | Risk Service |
| portfolio | Portfolio Service |
| knowledge | Knowledge Service |
| learning | Learning Service |
| reporting | Reporting Service |
| auth | Authentication Service |
| config | Configuration Service |
| audit | Audit Service |

---

# Master Table Inventory

## market

| Table |
|--------|
| market_state |
| market_snapshot |
| sector_state |
| market_event |
| trading_calendar |

---

## scanner

| Table |
|--------|
| scan_job |
| scan_result |
| watchlist |
| scanner_rule |

---

## setup

| Table |
|--------|
| setup |
| setup_pattern |
| setup_candidate |

---

## probability

| Table |
|--------|
| probability_assessment |
| confidence_calibration |
| historical_similarity |

---

## decision

| Table |
|--------|
| investment_case |
| committee_vote |
| decision |

---

## validation

| Table |
|--------|
| validation_report |
| validation_rule |

---

## risk

| Table |
|--------|
| risk_profile |
| risk_limit |
| exposure |

---

## portfolio

| Table |
|--------|
| portfolio |
| portfolio_position |
| trade |
| cash_transaction |

---

## knowledge

| Table |
|--------|
| lesson |
| knowledge |
| decision_history |

---

## learning

| Table |
|--------|
| learning |
| model_version |
| calibration_history |

---

## reporting

| Table |
|--------|
| report |
| report_execution |
| dashboard_snapshot |

---

## auth

| Table |
|--------|
| user |
| role |
| permission |
| refresh_token |

---

## audit

| Table |
|--------|
| audit_log |
| event_log |
| api_log |

---

# Standard Columns

Every table contains

```sql
id UUID PRIMARY KEY

created_at TIMESTAMP

updated_at TIMESTAMP

created_by UUID

version INTEGER

status VARCHAR(50)
```

Optional

```
deleted_at

deleted_by

tags JSONB
```

---

# Naming Standards

Schemas

```
snake_case
```

Tables

```
snake_case
```

Columns

```
snake_case
```

Indexes

```
idx_table_column
```

Constraints

```
fk_table_reference

pk_table

uk_table_column
```

---

# Relationships

Within a schema

Foreign Keys

Across schemas

UUID References

APIs

Domain Events

---

# UUID Strategy

ATHENA uses

UUID Version 7

for

- scalability
- ordering
- distributed systems

---

# JSON Usage

Use JSONB only for

- metadata
- tags
- dynamic AI outputs

Business data belongs in normalized columns.

---

# Partitioned Tables

Large tables

- market_snapshot
- trade
- report_execution
- audit_log

Partition

Monthly

---

# Read Models

Materialized Views

Examples

```
mv_market_summary

mv_portfolio_performance

mv_strategy_statistics
```

---

# Migration Strategy

Every schema has

```
V001

V002

V003
```

Migration folders

```
database/migrations/

market/

portfolio/

risk/
```

---

# Directory Structure

```
database/

schemas/

market/

portfolio/

knowledge/

migrations/

seed/

functions/

views/

materialized_views/
```

---

# Future Evolution

Future schemas

```
options

futures

crypto

international

ml

analytics
```

No existing schema requires redesign.

---

# References

- DATABASE_ARCHITECTURE.md
- DOMAIN_SCHEMA_MAP.md
- DATA_MODEL.md

---

## Detailed Schema Specifications

The following documents define every table, column,
constraint, relationship and index.

```
schemas/

market.sql.md

scanner.sql.md

setup.sql.md

probability.sql.md

decision.sql.md

validation.sql.md

risk.sql.md

portfolio.sql.md

knowledge.sql.md

learning.sql.md

reporting.sql.md

auth.sql.md

audit.sql.md
```

---

**End of Document**
