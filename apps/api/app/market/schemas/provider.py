from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MarketSnapshotData(BaseModel):
    """Normalized market data supplied to future Market services."""

    model_config = ConfigDict(frozen=True)

    snapshot_time: datetime
    nifty50: float = Field(gt=0)
    sensex: float = Field(gt=0)
    india_vix: float = Field(gt=0)
    advance_decline_ratio: float = Field(gt=0)
    breadth_score: float = Field(ge=0, le=100)
    market_health_score: float = Field(ge=0, le=100)


class SectorStrengthData(BaseModel):
    """A single ranked sector observation from a Market data provider."""

    model_config = ConfigDict(frozen=True)

    sector_name: str = Field(min_length=1, max_length=100)
    rank: int = Field(ge=1, le=10)
    strength_score: float = Field(ge=0, le=100)
    momentum_score: float


class MarketRegimeData(BaseModel):
    """Provider-supplied market-regime observation without persistence concerns."""

    model_config = ConfigDict(frozen=True)

    regime: str = Field(pattern="^(BULL|BEAR|SIDEWAYS)$")
    confidence: float = Field(ge=0, le=100)
    reason: str = Field(min_length=1, max_length=500)
