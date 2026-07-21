from datetime import datetime, timezone
from math import ceil

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.market.dependencies import get_market_service
from app.market.models import MarketSnapshot
from app.market.schemas import ApiResponse, CurrentMarketStateResponse, MarketLatestResponse, MarketRegimeResponse, MarketSnapshotResponse, PaginationMetadata, SectorStrengthResponse
from app.market.service import MarketPersistenceError, MarketProviderError, MarketService

router = APIRouter(prefix="/api/v1/market", tags=["market"])


def serialize_snapshot(snapshot: MarketSnapshot, service: MarketService) -> MarketSnapshotResponse:
    response_model = MarketSnapshotResponse.model_validate(snapshot)
    regime = service.get_snapshot_regime(snapshot)
    return response_model.model_copy(update={"regime_confidence": float(regime.confidence) if regime else None, "regime_reason": regime.reason if regime else None})


def response(data: MarketSnapshotResponse | CurrentMarketStateResponse | list[MarketSnapshotResponse], metadata: PaginationMetadata | None = None) -> ApiResponse:
    return ApiResponse(data=data, metadata=metadata, timestamp=datetime.now(timezone.utc))


@router.post("/refresh", response_model=ApiResponse, status_code=status.HTTP_200_OK, summary="Refresh the Market snapshot")
def refresh_market(service: MarketService = Depends(get_market_service)) -> ApiResponse:
    try:
        return response(serialize_snapshot(service.refresh_market(), service))
    except (MarketProviderError, MarketPersistenceError) as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Market refresh failed") from error


@router.get("/latest", response_model=MarketLatestResponse, summary="Get the latest Market snapshot")
def get_latest_market(service: MarketService = Depends(get_market_service)) -> MarketLatestResponse:
    state = service.get_latest_market_state()
    if state is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Market snapshot exists")
    snapshot, regime, sectors = state
    data = CurrentMarketStateResponse(snapshot=serialize_snapshot(snapshot, service), regime=MarketRegimeResponse(value=snapshot.market_regime, confidence=float(regime.confidence) if regime else None, reason=regime.reason if regime else None), sectors=[SectorStrengthResponse(rank=sector.rank, name=sector.sector_name, strength=float(sector.strength_score), momentum=float(sector.momentum_score)) for sector in sectors])
    return MarketLatestResponse(data=data, timestamp=datetime.now(timezone.utc))


@router.get("/history", response_model=ApiResponse, summary="Get paginated Market snapshot history")
def get_market_history(page: int = Query(default=1, ge=1), page_size: int = Query(default=20, ge=1, le=100), service: MarketService = Depends(get_market_service)) -> ApiResponse:
    snapshots = service.list_market_history()
    total_records = len(snapshots)
    start = (page - 1) * page_size
    items = [serialize_snapshot(snapshot, service) for snapshot in snapshots[start : start + page_size]]
    return response(items, PaginationMetadata(page=page, page_size=page_size, total_records=total_records, total_pages=ceil(total_records / page_size) if total_records else 0))
