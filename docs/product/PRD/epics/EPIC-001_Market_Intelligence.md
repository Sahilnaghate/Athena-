# EPIC-001 — Market Intelligence

> "Understand the market before understanding the stock."

---

| Property | Value |
|----------|-------|
| Epic ID | EPIC-001 |
| Epic Name | Market Intelligence |
| Version | 1.0.0 |
| Status | Draft |
| Priority | Critical |
| Owner | ATHENA Labs |
| Depends On | None |
| Required By | Scanner, Probability, Decision, Risk |

---

# Executive Summary

The Market Intelligence Engine is the first stage of ATHENA's decision pipeline.

Its responsibility is **not to identify trading opportunities**.

Its responsibility is to determine:

> **"What kind of market are we operating in today?"**

Every downstream engine depends on this answer.

No stock recommendation shall be produced before the Market Intelligence Engine completes its analysis.

---

# Business Objective

Provide a complete understanding of current market conditions before any investment decision is made.

The engine should answer:

- Is the market bullish, bearish or sideways?
- How healthy is the current trend?
- Which sectors are leading?
- Is volatility acceptable?
- Is today suitable for trading?
- Should capital exposure increase or decrease?

---

# Business Value

Without market context:

- Good stocks are bought in bad markets.
- Weak sectors are selected.
- Risk increases.
- Win rate decreases.

The Market Intelligence Engine reduces these mistakes.

---

# Success Criteria

The engine succeeds when it consistently provides:

- Accurate market regime classification.
- Reliable sector ranking.
- Timely identification of risk events.
- Consistent market health score.
- Actionable market guidance.

---

# Scope

Included

- NIFTY analysis
- BANKNIFTY analysis
- India VIX
- Sector rotation
- Market breadth
- Advance/Decline
- FII/DII activity
- RBI calendar
- Earnings calendar
- Global market overview
- Trading calendar
- Holiday awareness

Excluded (Version 1)

- Options Open Interest
- Futures positioning
- Global macro forecasting
- Machine learning prediction

---

# Inputs

## Market Data

NIFTY

BANKNIFTY

NIFTY 500

Sector Indices

---

## Breadth

Advance

Decline

52 Week High

52 Week Low

---

## Volatility

India VIX

ATR

Realized Volatility

---

## Institutional Activity

FII

DII

Net Buying

---

## Events

RBI

Budget

Election

Major Earnings

Economic Calendar

---

## Global Markets

US

Europe

Asia

USDINR

Crude Oil

Gold

Bond Yield

---

# Outputs

The engine produces:

## Market Regime

Possible values

- Strong Bull
- Bull
- Neutral
- Sideways
- Bear
- Strong Bear

---

## Market Health Score

Range

0–100

---

## Trading Environment

- Excellent
- Good
- Cautious
- High Risk
- Avoid

---

## Sector Ranking

Rank every sector.

Example

| Rank | Sector | Score |
|------|--------|------:|
| 1 | Pharma | 91 |
| 2 | Metal | 89 |
| 3 | Auto | 82 |
| ... | ... | ... |

---

## Volatility Score

Low

Medium

High

Extreme

---

## Exposure Recommendation

Example

Maximum Portfolio Exposure

20%

40%

60%

80%

---

# Modules

The Market Intelligence Engine contains nine modules.

---

## Module 1

Market Regime Detection

Responsibilities

Determine:

- Bull
- Bear
- Sideways

Inputs

EMA

Trend

Breadth

Outputs

Market Regime

---

## Module 2

Market Health

Calculates

Market Score

Trend Quality

Momentum

Liquidity

Participation

Output

0–100

---

## Module 3

Sector Rotation

Ranks every sector.

Outputs

Top sectors

Weak sectors

Rotation direction

---

## Module 4

Volatility

Analyzes

India VIX

ATR

Historical Volatility

Outputs

Risk Level

---

## Module 5

Market Breadth

Calculates

Advance Decline

High Low Ratio

Participation

---

## Module 6

Institutional Flow

Tracks

FII

DII

Net Flow

Trend

---

## Module 7

Economic Calendar

Checks

RBI

GDP

CPI

Fed

Budget

Expiry

Outputs

Risk Events

---

## Module 8

Global Markets

Tracks

Dow

NASDAQ

S&P

Nikkei

Hang Seng

Crude

Gold

USDINR

---

## Module 9

Trading Calendar

Determines

Holiday

Expiry

Settlement

Half Day

Trading Session

---

# Dependencies

Produces data for

- Scanner Engine
- Probability Engine
- Decision Engine
- Risk Engine
- Portfolio Engine

---

# Functional Features

FEATURE-001

Market Regime

---

FEATURE-002

Market Health Score

---

FEATURE-003

Sector Ranking

---

FEATURE-004

Volatility Assessment

---

FEATURE-005

Institutional Flow

---

FEATURE-006

Market Breadth

---

FEATURE-007

Global Market Analysis

---

FEATURE-008

Economic Events

---

FEATURE-009

Exposure Recommendation

---

# User Stories

As a swing trader,

I want ATHENA to tell me if today's market is suitable for trading,

so that I avoid taking positions during poor market conditions.

---

As an investor,

I want sectors ranked,

so that I focus only on strong sectors.

---

As a portfolio manager,

I want ATHENA to recommend maximum exposure,

so that my portfolio risk adjusts to market conditions.

---

# Acceptance Criteria

The engine shall:

✓ Detect current market regime.

✓ Calculate Market Health Score.

✓ Rank all supported sectors.

✓ Detect major risk events.

✓ Generate exposure recommendation.

✓ Complete within acceptable response time.

---

# Risks

Possible failures

Incorrect regime detection

Missing market data

Delayed institutional data

Holiday calendar mismatch

Incorrect sector ranking

Mitigation

Fallback providers

Data validation

Health monitoring

Manual override

---

# Future Enhancements

Machine Learning Regime Detection

Market Sentiment AI

Options Open Interest

Global Correlation Engine

Macro Forecasting

Multi-timeframe Regime Analysis

---

# Definition of Done

The Epic is complete when:

- All modules implemented.
- Unit tests pass.
- APIs documented.
- Database schema approved.
- Integration tests pass.
- Documentation updated.
- Founder approval obtained.

---

# Related Documents

- PRODUCT_REQUIREMENTS.md
- QUANTITATIVE_FRAMEWORK.md
- DATA_GOVERNANCE.md
- ENGINEERING_STANDARDS.md
