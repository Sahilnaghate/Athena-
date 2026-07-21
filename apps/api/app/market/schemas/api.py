from datetime import datetime
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MarketSnapshotResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    snapshot_time: datetime
    market_status: str
    market_regime: str
    market_health_score: float
    advance_decline_ratio: float
    volatility_index: float
    breadth_score: float
    regime_confidence: float | None = None
    regime_reason: str | None = None


class PaginationMetadata(BaseModel):
    page: int = Field(ge=1)
    page_size: int = Field(ge=1)
    total_records: int = Field(ge=0)
    total_pages: int = Field(ge=0)


ResponseData = TypeVar("ResponseData")


class ApiResponse(BaseModel, Generic[ResponseData]):
    success: bool = True
    data: ResponseData
    metadata: PaginationMetadata | None = None
    timestamp: datetime


class MarketRegimeResponse(BaseModel):
    value: str
    confidence: float | None
    reason: str | None


class SectorStrengthResponse(BaseModel):
    rank: int
    name: str
    strength: float
    momentum: float


class CurrentMarketStateResponse(BaseModel):
    snapshot: MarketSnapshotResponse
    regime: MarketRegimeResponse
    sectors: list[SectorStrengthResponse]


class MarketLatestResponse(ApiResponse[CurrentMarketStateResponse]):
    """Typed response envelope for the complete current Market state."""
