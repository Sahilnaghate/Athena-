# ATHENA REST API Conventions

> **Standard conventions for designing RESTful APIs in ATHENA**

---

| Property | Value |
|----------|-------|
| Document | REST_CONVENTIONS.md |
| Document ID | ATH-API-002 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | API Standards |
| Depends On | API_DESIGN_GUIDELINES.md |

---

# Purpose

This document defines the REST conventions used throughout ATHENA.

Its objective is to ensure that every endpoint follows a predictable,
consistent and REST-compliant structure.

---

# REST Principles

ATHENA APIs are:

- Resource Oriented
- Stateless
- Cache Friendly
- Uniform
- Versioned
- Discoverable

---

# Base URL

```
https://api.athena.ai/api/v1/
```

Development

```
http://localhost:8000/api/v1/
```

---

# Resource Naming

Always use plural nouns.

Correct

```
/markets

/stocks

/setups

/decisions

/trades

/portfolios
```

Wrong

```
/getTrades

/getPortfolio

/createTrade

/tradeList
```

---

# URI Structure

```
/api/v1/{resource}

/api/v1/{resource}/{id}

/api/v1/{resource}/{id}/{child-resource}
```

Examples

```
/api/v1/trades

/api/v1/trades/{tradeId}

/api/v1/portfolios/{portfolioId}/positions
```

---

# HTTP Methods

GET

Retrieve data

Example

```
GET /api/v1/trades
```

---

POST

Create new resource

```
POST /api/v1/trades
```

---

PUT

Replace entire resource

```
PUT /api/v1/trades/{tradeId}
```

---

PATCH

Partial update

```
PATCH /api/v1/trades/{tradeId}
```

---

DELETE

Delete resource

```
DELETE /api/v1/trades/{tradeId}
```

---

# Collection Endpoints

Retrieve all resources

```
GET /api/v1/stocks
```

Supports

- Pagination
- Filtering
- Sorting
- Searching

---

# Single Resource

```
GET /api/v1/stocks/{stockId}
```

Returns one resource.

---

# Nested Resources

Portfolio

↓

Positions

```
GET

/api/v1/portfolios/{portfolioId}/positions
```

Decision

↓

Trades

```
GET

/api/v1/decisions/{decisionId}/trades
```

---

# Query Parameters

Filtering

```
?status=OPEN
```

Multiple filters

```
?status=OPEN&symbol=TCS
```

Searching

```
?search=reliance
```

Sorting

```
?sort=entry_date
```

Descending

```
?sort=-entry_date
```

Pagination

```
?page=1&page_size=20
```

---

# Resource IDs

Every resource uses UUID.

Example

```
GET

/api/v1/trades/

550e8400-e29b-41d4-a716-446655440000
```

Sequential IDs are prohibited.

---

# Standard Endpoints

Collection

```
GET

POST
```

Single Resource

```
GET

PATCH

DELETE
```

Avoid custom verbs whenever possible.

---

# Bulk Operations

Use dedicated endpoints.

```
POST

/api/v1/trades/bulk

POST

/api/v1/stocks/import
```

---

# Actions

Actions that cannot be represented by CRUD should be explicit.

Examples

```
POST

/api/v1/strategies/{id}/backtest

POST

/api/v1/portfolio/rebalance

POST

/api/v1/decision/{id}/approve
```

---

# Response Codes

| Code | Meaning |
|------|---------|
|200|OK|
|201|Created|
|202|Accepted|
|204|No Content|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|409|Conflict|
|422|Validation Error|
|429|Rate Limited|
|500|Internal Error|

---

# Standard Success Response

```json
{
  "success": true,
  "data": {},
  "metadata": {
    "request_id": "req_123456",
    "timestamp": "2026-07-18T10:30:00Z"
  }
}
```

---

# Standard Error Response

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Entry price is required."
  },
  "request_id": "req_123456"
}
```

---

# Pagination Format

```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total_records": 150,
    "total_pages": 8
  }
}
```

---

# API Versioning

Current

```
/api/v1/
```

Future

```
/api/v2/
```

Version is mandatory.

---

# Idempotency

Financial APIs must support

```
Idempotency-Key
```

Header

```
Idempotency-Key:
4cf8d42c
```

---

# Correlation ID

Every request contains

```
X-Correlation-ID
```

Used for

- tracing
- debugging
- event correlation

---

# Security

REST APIs require

- HTTPS
- JWT
- RBAC
- Validation
- Rate Limiting
- Audit Logging

---

# Anti-Patterns

Do NOT use

```
GET /getTrades

POST /updateTrade

GET /createTrade

POST /deletePortfolio
```

Instead

```
GET /trades

PATCH /trades/{id}

DELETE /portfolios/{id}
```

---

# REST Compliance Checklist

Every endpoint shall:

- Represent one resource
- Use the correct HTTP method
- Return standard status codes
- Support OpenAPI documentation
- Validate input
- Return consistent responses
- Publish events when applicable

---

# References

- API_DESIGN_GUIDELINES.md
- AUTHENTICATION.md
- ERROR_HANDLING.md
- API_SPECIFICATION.md

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
|1.0.0|July 2026|Initial REST API conventions|

---

**End of Document**
