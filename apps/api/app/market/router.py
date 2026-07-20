from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.market.calculators import MarketHealthCalculator, MarketRegimeDetector
from app.market.provider import MockMarketDataProvider
from app.market.repository import MarketRepository
from app.market.service import MarketService

router = APIRouter(prefix="/api/v1/market", tags=["market"])


class ApiResponse(BaseModel):
    success: bool = True
    data: object
    metadata: dict[str, object] = {}
    timestamp: datetime


def get_market_service(session: Session = Depends(get_db)) -> MarketService:
    return MarketService(MarketRepository(session), MockMarketDataProvider(), MarketHealthCalculator(), MarketRegimeDetector())


def response(data: object) -> ApiResponse:
    return ApiResponse(data=data, timestamp=datetime.now(timezone.utc))


@router.get("/overview", response_model=ApiResponse, summary="Get market overview")
async def overview(service: MarketService = Depends(get_market_service)) -> ApiResponse:
    return response(service.overview())


@router.get("/regime", response_model=ApiResponse, summary="Get current market regime")
async def regime(service: MarketService = Depends(get_market_service)) -> ApiResponse:
    return response(service.regime())


@router.get("/sectors", response_model=ApiResponse, summary="Get sector strength ranking")
async def sectors(service: MarketService = Depends(get_market_service)) -> ApiResponse:
    return response(service.sectors())


@router.post("/refresh", response_model=ApiResponse, summary="Refresh market data from the configured provider")
async def refresh(service: MarketService = Depends(get_market_service)) -> ApiResponse:
    return response(await service.refresh())
