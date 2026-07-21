import logging

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.market.providers import MarketDataProvider, MockMarketDataProvider
from app.market.repository import MarketRepository
from app.market.service import MarketService


def get_market_provider() -> MarketDataProvider:
    """Select the configured provider at the composition root."""
    return MockMarketDataProvider()


def get_market_service(session: Session = Depends(get_db), provider: MarketDataProvider = Depends(get_market_provider)) -> MarketService:
    """Inject Market dependencies outside of request controllers."""
    return MarketService(provider, MarketRepository(session), logging.getLogger("athena.api"))
