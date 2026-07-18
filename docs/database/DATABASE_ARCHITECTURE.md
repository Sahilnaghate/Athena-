# ATHENA Database Architecture

> **The authoritative database architecture for ATHENA**

---

| Property | Value |
|----------|-------|
| Document | DATABASE_ARCHITECTURE.md |
| Document ID | ATH-DB-001 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | Database Architecture |
| Depends On | DATA_MODEL.md |
| Related Documents | POSTGRES_SCHEMA.md, INDEXING_STRATEGY.md |

---

# Purpose

This document defines the database architecture for ATHENA.

It establishes:

- Database principles
- Schema organization
- Ownership
- Transactions
- Performance strategy
- Scalability
- Security
- Disaster recovery

This document is technology-aware and assumes PostgreSQL as the primary database.

---

# Database Philosophy

ATHENA follows these principles.

1. Data is an Asset
2. One Owner per Entity
3. Immutable Historical Records
4. ACID for Financial Data
5. Event Driven Integration
6. Read Optimized Analytics
7. Write Optimized Transactions

---

# Database Technology Stack

| Component | Technology |
|------------|------------|
| Primary Database | PostgreSQL |
| Cache | Redis |
| Object Storage | S3 Compatible Storage |
| Search | PostgreSQL Full Text (Future: Elasticsearch) |
| Graph (Future) | Neo4j |
| Analytics | PostgreSQL Materialized Views |

---

# High-Level Architecture

```text
                  Applications

                         │

                         ▼

                 API / Services

                         │

──────────────────────────────────────────

               PostgreSQL

──────────────────────────────────────────

Operational Data

Knowledge Data

Audit Data

Configuration

Reporting

──────────────────────────────────────────

Redis Cache

──────────────────────────────────────────

Object Storage

──────────────────────────────────────────

Backups
```

---

# Database Schemas

ATHENA separates data into logical schemas.

| Schema | Purpose |
|----------|----------|
| market | Market information |
| scanner | Scanner results |
| setup | Trading setups |
| probability | Probability engine |
| decision | Investment decisions |
| validation | Validation reports |
| risk | Risk calculations |
| portfolio | Portfolio management |
| knowledge | Knowledge graph |
| learning | Learning artifacts |
| reporting | Reports |
| auth | Users & authentication |
| config | System configuration |
| audit | Audit logs |

---

# Schema Ownership

Every schema has one owning service.

| Schema | Owner |
|----------|-------|
| market | Market Intelligence |
| scanner | Scanner Service |
| setup | Setup Service |
| probability | Probability Service |
| decision | Decision Service |
| validation | Validation Service |
| risk | Risk Service |
| portfolio | Portfolio Service |
| knowledge | Knowledge Service |
| learning | Learning Service |
| reporting | Reporting Service |

No service writes directly into another service's schema.

---

# Data Classification

| Classification | Examples |
|---------------|-----------|
| Reference | Stocks, Sectors |
| Transactional | Trades, Positions |
| Analytical | Reports |
| Configuration | Settings |
| Knowledge | Lessons |
| Audit | Logs |

---

# Table Design Principles

Every table must include:

```text
id

created_at

updated_at

version

created_by

status
```

Optional

```text
deleted_at

deleted_by

tags
```

---

# Primary Keys

Rules

- UUID v7 preferred
- Never use sequential IDs
- IDs are immutable

---

# Foreign Keys

Use foreign keys inside the same schema.

Cross-schema references should be minimized and accessed through services or well-defined contracts.

---

# Transactions

Financial operations require ACID transactions.

Examples

- Trade execution
- Portfolio updates
- Cash balance updates

Reporting queries should not block transactional workloads.

---

# Read / Write Strategy

Write

Optimized for:

- Trade execution
- Portfolio updates
- Decision recording

Read

Optimized for:

- Dashboards
- Reports
- Analytics
- AI queries

---

# Indexing Philosophy

Indexes should exist for:

- Primary Keys
- Foreign Keys
- Frequently filtered columns
- Time-series queries

Avoid excessive indexing that slows writes.

Detailed indexing strategy is defined in `INDEXING_STRATEGY.md`.

---

# Partitioning Strategy

Large tables should be partitioned by time.

Examples

- market.market_data
- portfolio.trades
- reporting.report_history
- audit.audit_log

Recommended partition

Monthly

Future

Weekly for high-volume datasets.

---

# Soft Delete Policy

Transactional entities

Use soft delete.

Reference data

Avoid deletion.

Audit data

Never delete.

---

# Audit Strategy

Every financial action must be traceable.

Audit captures

- User
- Action
- Timestamp
- Before Value
- After Value
- Correlation ID

Audit records are immutable.

---

# Caching Strategy

Redis stores:

- Market snapshots
- Feature Store cache
- Frequently accessed portfolios
- Active watchlists
- Authentication sessions

Redis is never the source of truth.

---

# Backup Strategy

Daily full backup

Hourly incremental backup

Point-in-time recovery enabled

Backups encrypted at rest.

---

# Disaster Recovery

Recovery Point Objective (RPO)

≤ 15 minutes

Recovery Time Objective (RTO)

≤ 1 hour

---

# Data Retention

| Data | Retention |
|------|-----------|
| Trades | Permanent |
| Decisions | Permanent |
| Knowledge | Permanent |
| Reports | 10 Years |
| Market Data | 10 Years |
| Audit Logs | Permanent |
| Sessions | 30 Days |

---

# Security

Database security requirements

- TLS connections
- Encryption at rest
- Row-Level Security (where applicable)
- Principle of Least Privilege
- Read-only reporting users
- Secret management
- Audit logging

---

# Performance Targets

| Operation | Target |
|------------|---------|
| Insert Trade | <100 ms |
| Portfolio Query | <200 ms |
| Market Snapshot | <100 ms |
| Dashboard Load | <2 sec |
| Report Generation | <30 sec |

---

# Database Lifecycle

```text
Business Entity

↓

Logical Model

↓

Physical Schema

↓

Migration

↓

Production

↓

Monitoring

↓

Optimization
```

---

# Future Evolution

The architecture supports:

- Multi-Tenant SaaS
- Multi-Exchange
- Multi-Asset
- Read Replicas
- Partitioned Tables
- Distributed Caching
- Event Sourcing
- Graph Database Integration

---

# References

- DATA_MODEL.md
- ENTITY_RELATIONSHIP.md
- DATA_DICTIONARY.md
- FEATURE_STORE.md
- EVENT_CATALOG.md
- POSTGRES_SCHEMA.md
- INDEXING_STRATEGY.md

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | July 2026 | Initial Database Architecture |

---

**End of Document**
