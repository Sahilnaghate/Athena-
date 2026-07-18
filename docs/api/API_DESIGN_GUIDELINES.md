# ATHENA API Design Guidelines

> **The API Constitution for ATHENA**

---

| Property | Value |
|----------|-------|
| Document | API_DESIGN_GUIDELINES.md |
| Document ID | ATH-API-001 |
| Version | 1.0.0 |
| Status | Draft |
| Owner | ATHENA Labs |
| Classification | API Architecture |
| Depends On | ATHENA_SYSTEM_ARCHITECTURE.md |
| Related Documents | REST_CONVENTIONS.md, AUTHENTICATION.md, ERROR_HANDLING.md |

---

# Purpose

This document defines the standards and principles used to design every API exposed by ATHENA.

Its goals are to ensure APIs are:

- Consistent
- Predictable
- Secure
- Versioned
- Self-documenting
- Easy to maintain

Every API developed within ATHENA must comply with these guidelines.

---

# API Design Principles

ATHENA APIs follow these principles:

1. Resource-Oriented
2. Stateless
3. RESTful
4. Versioned
5. Secure by Default
6. Consistent
7. Backward Compatible
8. OpenAPI First
9. Event Driven
10. Idempotent where applicable

---

# API Architecture

```
Client

↓

API Gateway

↓

Authentication

↓

Authorization

↓

Validation

↓

Business Service

↓

Database

↓

Domain Event

↓

Response
```

---

# Base URL

```
/api/v1/
```

Examples

```
/api/v1/markets

/api/v1/sectors

/api/v1/stocks

/api/v1/setups

/api/v1/probabilities

/api/v1/investment-cases

/api/v1/decisions

/api/v1/portfolios

/api/v1/trades
```

---

# Resource Naming

Use plural nouns.

Correct

```
/markets

/sectors

/trades

/portfolios

/users
```

Incorrect

```
/getTrades

/getPortfolio

/createTrade

/updatePortfolio
```

---

# HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve resource |
| POST | Create resource |
| PUT | Replace resource |
| PATCH | Partial update |
| DELETE | Remove resource |

---

# URI Standards

Single Resource

```
GET

/api/v1/trades/{tradeId}
```

Collection

```
GET

/api/v1/trades
```

Nested Resource

```
GET

/api/v1/portfolios/{portfolioId}/positions
```

---

# Resource Identifiers

Every resource uses UUID.

Example

```
/api/v1/trades/

550e8400-e29b-41d4-a716-446655440000
```

Never expose database IDs.

---

# Standard Request Headers

```
Authorization

Content-Type

Accept

Correlation-ID

Request-ID

User-Agent
```

---

# Standard Response Structure

Every successful response follows:

```json
{
  "success": true,
  "data": {},
  "metadata": {},
  "timestamp": "2026-07-18T10:30:00Z"
}
```

---

# Error Response

Every error response follows:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Portfolio ID is required.",
    "details": []
  },
  "timestamp": "2026-07-18T10:30:00Z",
  "request_id": "req_123456"
}
```

---

# Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation Error |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

# Pagination

Collections must support pagination.

Request

```
GET /api/v1/trades?page=1&page_size=20
```

Response

```json
{
  "success": true,
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

# Filtering

Use query parameters.

Examples

```
GET /api/v1/trades?status=OPEN

GET /api/v1/trades?symbol=TCS

GET /api/v1/trades?portfolio=swing
```

---

# Sorting

```
GET /api/v1/trades?sort=entry_date

GET /api/v1/trades?sort=-entry_date
```

Ascending

```
sort=entry_date
```

Descending

```
sort=-entry_date
```

---

# Searching

```
GET /api/v1/stocks?search=reliance
```

---

# Versioning

API version appears in the URL.

```
/api/v1/

/api/v2/
```

Breaking changes require a new version.

---

# Authentication

All APIs require authentication except:

- Health Check
- Login
- Token Refresh

Authentication uses JWT Bearer Tokens.

Example

```
Authorization: Bearer <token>
```

---

# Authorization

Role-Based Access Control (RBAC)

Roles

- Founder
- Admin
- Analyst
- Trader
- Researcher
- Viewer

Every endpoint defines required roles.

---

# Validation Rules

Every request must validate:

- Required fields
- Data types
- Business rules
- Authorization
- Ownership

Validation happens before business logic.

---

# Idempotency

POST endpoints that create financial transactions must support idempotency.

Example Header

```
Idempotency-Key: 7f83b165
```

---

# Correlation IDs

Every request receives a Correlation ID.

Example

```
X-Correlation-ID
```

Used for:

- Logging
- Event tracing
- Distributed debugging

---

# Event Publishing

Business APIs publish domain events.

Example

```
POST /trades

↓

TradeCreated Event
```

Consumers

- Reporting
- Knowledge
- Learning

---

# Rate Limiting

Default

```
100 requests/minute/user
```

Burst

```
200 requests
```

Admin APIs may have higher limits.

---

# OpenAPI

Every endpoint must be documented using OpenAPI 3.1.

Documentation includes:

- Summary
- Parameters
- Request
- Response
- Errors
- Examples

---

# Security

Requirements

- HTTPS only
- JWT Authentication
- Input Validation
- SQL Injection Protection
- XSS Protection
- CSRF Protection (where applicable)
- Rate Limiting
- Audit Logging

---

# Logging

Every API request logs:

- Request ID
- Correlation ID
- User
- Endpoint
- Method
- Response Code
- Duration

Sensitive data must never be logged.

---

# API Lifecycle

```
Design

↓

Review

↓

Approval

↓

Implementation

↓

Testing

↓

Documentation

↓

Deployment

↓

Monitoring

↓

Deprecation
```

---

# API Quality Checklist

Every endpoint must:

- Follow REST conventions
- Validate input
- Return standard responses
- Publish events where applicable
- Include OpenAPI documentation
- Support monitoring
- Pass automated tests
- Follow security guidelines

---

# References

- ATHENA_SYSTEM_ARCHITECTURE.md
- ATHENA_SERVICE_CATALOG.md
- DATA_MODEL.md
- EVENT_CATALOG.md
- REST_CONVENTIONS.md
- AUTHENTICATION.md
- ERROR_HANDLING.md

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | July 2026 | Initial API Design Guidelines |

---

**End of Document**
