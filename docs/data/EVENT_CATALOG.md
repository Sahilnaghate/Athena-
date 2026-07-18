# ATHENA Event Catalog

> **The authoritative specification for all domain events published and consumed by ATHENA services.**

---

| Property | Value |
|----------|-------|
| Document | EVENT_CATALOG.md |
| Document ID | ATH-DATA-006 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | Event Architecture |
| Depends On | DATA_MODEL.md |
| Related Documents | ENTITY_RELATIONSHIP.md, ATHENA_SERVICE_CATALOG.md |

---

# Purpose

ATHENA follows an Event-Driven Architecture (EDA).

Services never directly manipulate another service's data.

Instead they communicate through immutable domain events.

This document defines every event used across the platform.

---

# Event Architecture

```text
Producer Service

↓

Domain Event

↓

Event Bus

↓

Subscriber Services

↓

Local Processing
```

---

# Event Design Principles

Every event must:

- Represent something that already happened
- Be immutable
- Be versioned
- Have exactly one producer
- Support multiple consumers
- Be replayable
- Be auditable

---

# Event Naming Convention

```
<Entity><PastTenseVerb>
```

Examples

```
MarketRegimeChanged

SetupDetected

ProbabilityCalculated

DecisionApproved

TradeExecuted

LessonCreated
```

---

# Event Envelope

Every event contains:

| Field | Type | Description |
|---------|------|-------------|
| event_id | UUID | Unique event ID |
| event_name | String | Event name |
| event_version | Integer | Version |
| occurred_at | Timestamp | UTC time |
| producer | String | Producing service |
| correlation_id | UUID | Workflow identifier |
| payload | JSON | Business data |

---

# Event Lifecycle

```text
Business Action

↓

Domain Event

↓

Event Bus

↓

Consumers

↓

Processing

↓

Audit Log
```

---

# SERVICE EVENTS

---

# Market Intelligence Service

Publishes

## MarketRegimeChanged

Description

Market regime changed.

Payload

- regime
- previous_regime
- confidence
- timestamp

Consumers

- Scanner
- Probability
- Decision
- Reporting

---

## MarketHealthUpdated

Payload

- health_score
- breadth
- volatility
- vix

Consumers

- Scanner
- Risk
- Reporting

---

## SectorRankingUpdated

Payload

- rankings
- strongest_sector
- weakest_sector

Consumers

- Scanner
- Portfolio

---

# Scanner Intelligence Service

Publishes

## SetupDetected

Payload

- setup_id
- symbol
- setup_type
- timeframe

Consumers

- Setup Intelligence

---

## WatchlistUpdated

Payload

- symbols
- additions
- removals

Consumers

- Portfolio
- Reporting

---

# Setup Intelligence Service

Publishes

## SetupValidated

Payload

- setup_id
- validation_score

Consumers

- Probability

---

## SetupExpired

Payload

- setup_id
- reason

Consumers

- Portfolio

---

# Probability Intelligence Service

Publishes

## ProbabilityCalculated

Payload

- setup_id
- probability
- confidence
- expected_return
- expected_drawdown

Consumers

- Investment Committee
- Decision

---

## ConfidenceUpdated

Payload

- confidence
- calibration_version

Consumers

- Learning

---

# Investment Committee Service

Publishes

## CommitteeRecommendationCreated

Payload

- investment_case
- votes
- committee_summary

Consumers

- Decision

---

# Investment Decision Service

Publishes

## DecisionApproved

Payload

- decision_id
- recommendation
- decision_score

Consumers

- Validation

---

## DecisionRejected

Payload

- reason
- investment_case

Consumers

- Knowledge

---

# Validation Intelligence Service

Publishes

## ValidationPassed

Payload

- validation_id
- approval_level

Consumers

- Risk

---

## ValidationFailed

Payload

- validation_id
- failure_reason

Consumers

- Knowledge

---

# Risk Intelligence Service

Publishes

## RiskCalculated

Payload

- position_size
- stop_loss
- portfolio_heat

Consumers

- Portfolio

---

## RiskLimitExceeded

Payload

- rule
- value

Consumers

- Decision
- Portfolio

---

# Portfolio Intelligence Service

Publishes

## TradeCreated

Payload

- trade_id
- symbol
- quantity

Consumers

- Broker Connector
- Reporting

---

## TradeExecuted

Payload

- trade_id
- execution_price

Consumers

- Knowledge

---

## PositionUpdated

Payload

- position_id
- pnl

Consumers

- Reporting

---

## PortfolioUpdated

Payload

- portfolio_value
- cash_balance

Consumers

- Reporting

---

# Knowledge Intelligence Service

Publishes

## LessonCreated

Payload

- lesson_id
- lesson_type
- summary

Consumers

- Learning

---

## KnowledgeUpdated

Payload

- knowledge_id
- category

Consumers

- AI Coach

---

# Learning Intelligence Service

Publishes

## ModelImproved

Payload

- model_name
- version

Consumers

- Probability
- Decision

---

## CalibrationUpdated

Payload

- calibration_version

Consumers

- Probability

---

# Strategy Lab

Publishes

## ExperimentCompleted

Payload

- experiment
- result

Consumers

- Reporting

---

## StrategyValidated

Payload

- strategy
- win_rate

Consumers

- Knowledge

---

# Reporting Service

Publishes

## ReportGenerated

Payload

- report_type
- generated_at

Consumers

- Notification

---

# Notification Service

Publishes

## NotificationSent

Payload

- notification_type
- recipient

---

# Event Ownership Matrix

| Event | Producer |
|--------|----------|
| MarketRegimeChanged | Market Intelligence |
| MarketHealthUpdated | Market Intelligence |
| SectorRankingUpdated | Market Intelligence |
| SetupDetected | Scanner |
| SetupValidated | Setup Intelligence |
| ProbabilityCalculated | Probability |
| CommitteeRecommendationCreated | Investment Committee |
| DecisionApproved | Decision |
| ValidationPassed | Validation |
| RiskCalculated | Risk |
| TradeCreated | Portfolio |
| TradeExecuted | Portfolio |
| LessonCreated | Knowledge |
| KnowledgeUpdated | Knowledge |
| ModelImproved | Learning |
| ExperimentCompleted | Strategy Lab |
| ReportGenerated | Reporting |

---

# Event Versioning

Rules

- Events are immutable.
- Breaking changes require a new version.
- Consumers must support backward compatibility.
- Historical events are never modified.

---

# Event Delivery Guarantees

ATHENA uses:

- At-Least-Once Delivery
- Idempotent Consumers
- Retry with Exponential Backoff
- Dead Letter Queue
- Event Replay

---

# Event Correlation

Every event contains:

```
correlation_id
```

This allows tracking an entire workflow.

Example

```
SetupDetected

↓

ProbabilityCalculated

↓

CommitteeRecommendationCreated

↓

DecisionApproved

↓

ValidationPassed

↓

RiskCalculated

↓

TradeExecuted

↓

LessonCreated

↓

KnowledgeUpdated
```

All linked by the same correlation ID.

---

# Audit Requirements

Every event must be:

- Logged
- Timestamped
- Versioned
- Traceable
- Searchable

Events are never deleted.

---

# Future Enhancements

Future versions may include:

- Apache Kafka
- Redis Streams
- RabbitMQ
- Event Sourcing
- CQRS
- Event Replay Dashboard
- Distributed Tracing (OpenTelemetry)

---

# References

- DATA_MODEL.md
- ENTITY_RELATIONSHIP.md
- FEATURE_STORE.md
- KNOWLEDGE_GRAPH.md
- ATHENA_SERVICE_CATALOG.md
- ATHENA_SYSTEM_ARCHITECTURE.md

---

**End of Document**
