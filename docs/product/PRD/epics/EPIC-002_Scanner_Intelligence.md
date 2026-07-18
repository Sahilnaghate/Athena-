# EPIC-002 — Scanner Intelligence

> **"Find opportunities that match ATHENA's philosophy, not just market movement."**

---

| Property | Value |
|----------|-------|
| Epic ID | EPIC-002 |
| Epic Name | Scanner Intelligence |
| Version | 1.0.0 |
| Status | Draft |
| Priority | Critical |
| Owner | ATHENA Labs |
| Depends On | EPIC-001 Market Intelligence |
| Required By | Probability Engine, Decision Engine |

---

# Executive Summary

The Scanner Intelligence Engine identifies investment opportunities after the Market Intelligence Engine has determined that market conditions are suitable.

Unlike traditional stock screeners, ATHENA's scanner is **context-aware**.

It never scans in isolation.

Every scan is filtered by:

- Market Regime
- Sector Strength
- Risk Rules
- Trading Style
- User Preferences

---

# Business Objective

Identify the highest-quality investment opportunities while eliminating low-probability setups.

The scanner must reduce noise rather than increase it.

---

# Business Value

Instead of returning hundreds of stocks, ATHENA should return only the highest-conviction candidates.

Quality over quantity.

---

# Scope

## Included (Version 1)

- Long Scanner
- Short Opportunity Scanner
- Dividend Scanner
- Breakout Scanner
- Pullback Scanner
- Trend Continuation Scanner
- Relative Strength Scanner
- Momentum Scanner
- Watchlist Scanner

## Excluded

- Options Scanner
- Futures Scanner
- Intraday Scalping Scanner
- Crypto Scanner

---

# Inputs

## Market Context

- Market Regime
- Market Health Score
- Sector Rankings
- Trading Environment

## Stock Data

- OHLCV
- Volume
- Market Capitalization
- Sector
- Industry

## Technical Indicators

- EMA 20
- EMA 50
- EMA 200
- RSI
- MACD
- ADX
- ATR
- VWAP
- Relative Strength
- Average Volume

## User Configuration

- Trading Style
- Holding Period
- Capital
- Maximum Risk
- Preferred Sectors
- Watchlist

---

# Outputs

The Scanner produces:

- Candidate List
- Opportunity Score
- Setup Type
- Suggested Entry Zone
- Suggested Stop Zone
- Suggested Target Zone
- Estimated Holding Period
- Scanner Confidence

---

# Scanner Categories

## Scanner 1

### Long Opportunity Scanner

Purpose

Find high-quality bullish opportunities.

Minimum Conditions

- Price > EMA50
- Price > EMA200
- Strong Sector
- Positive Relative Strength
- Healthy Volume
- Market Bull/Bullish

---

## Scanner 2

### Short Opportunity Scanner

Purpose

Find bearish opportunities (using supported instruments).

Conditions

- Price < EMA50
- Price < EMA200
- Weak Sector
- Negative Momentum
- High Distribution Volume

---

## Scanner 3

### Dividend Scanner

Purpose

Identify long-term dividend opportunities.

Conditions

- Sustainable Dividend
- Healthy Cash Flow
- Low Debt
- Acceptable Valuation
- Government Ownership (optional filter)

---

## Scanner 4

### Breakout Scanner

Purpose

Detect breakout candidates.

Checks

- Consolidation
- Volume Expansion
- Resistance Break
- Trend Confirmation

---

## Scanner 5

### Pullback Scanner

Purpose

Identify pullbacks within established trends.

Checks

- Pullback to EMA20/EMA50
- Trend Intact
- Volume Dry-Up
- Support Holding

---

## Scanner 6

### Trend Continuation Scanner

Purpose

Find continuation setups.

Checks

- Higher Highs
- Higher Lows
- Strong ADX
- Strong Relative Strength

---

## Scanner 7

### Relative Strength Scanner

Purpose

Identify stocks outperforming the index.

---

## Scanner 8

### Momentum Scanner

Purpose

Find accelerating momentum.

---

## Scanner 9

### Watchlist Scanner

Purpose

Continuously monitor user watchlists and notify when predefined conditions are met.

---

# Ranking Engine

Every candidate receives:

## Opportunity Score

Range

0–100

Components

- Trend
- Sector
- Momentum
- Volume
- Relative Strength
- Market Regime
- Risk
- Liquidity

---

# Filtering Pipeline

```
Market

↓

Sector

↓

Scanner

↓

Probability

↓

Risk

↓

Decision
```

Every candidate must pass each stage before progressing.

---

# Functional Features

FEATURE-101

Long Scanner

FEATURE-102

Short Scanner

FEATURE-103

Dividend Scanner

FEATURE-104

Breakout Scanner

FEATURE-105

Pullback Scanner

FEATURE-106

Trend Continuation

FEATURE-107

Relative Strength

FEATURE-108

Momentum

FEATURE-109

Watchlist

FEATURE-110

Opportunity Ranking

---

# User Stories

As a swing trader,

I want ATHENA to identify only high-quality opportunities,

so that I spend less time filtering charts.

---

As a dividend investor,

I want ATHENA to highlight fundamentally strong dividend-paying companies,

so that I can build a long-term portfolio.

---

As a positional trader,

I want ATHENA to continuously monitor my watchlist,

so that I receive timely notifications.

---

# Acceptance Criteria

The scanner shall:

- Respect current Market Regime.
- Exclude weak sectors.
- Rank opportunities.
- Produce explainable results.
- Complete scanning within configured performance limits.
- Return only validated candidates.

---

# Risks

- Excessive false positives
- Poor data quality
- Indicator lag
- Over-filtering
- Under-filtering

Mitigation

- Multi-factor scoring
- Probability Engine validation
- Continuous calibration
- Historical evaluation

---

# Dependencies

Depends On

- EPIC-001 Market Intelligence

Provides Data To

- EPIC-003 Probability Intelligence
- EPIC-004 Decision Intelligence
- EPIC-005 Risk Intelligence

---

# Future Enhancements

- Machine Learning Scanner
- Candlestick Pattern Scanner
- Sector Rotation Scanner
- Earnings Surprise Scanner
- Insider Activity Scanner
- AI Pattern Recognition
- Custom User Scanner Builder

---

# Definition of Done

This Epic is complete when:

- All scanners implemented.
- Ranking Engine operational.
- APIs documented.
- Test coverage exceeds project standards.
- Documentation approved.
- Founder acceptance completed.

---

# Related Documents

- EPIC-001 Market Intelligence
- QUANTITATIVE_FRAMEWORK.md
- DATA_GOVERNANCE.md
- ENGINEERING_STANDARDS.md
