from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.market.models import MarketRegime, MarketSnapshot, SectorStrength
from app.market.repository import MarketRepository

SECTORS = (("Financial Services", 89.5, 4.2), ("Information Technology", 84.0, 3.7), ("Healthcare", 78.5, 2.9), ("Consumer Goods", 74.0, 2.4), ("Automobile", 70.5, 1.8), ("Capital Goods", 68.0, 1.3), ("Oil & Gas", 64.5, 0.8), ("Metals", 61.0, 0.3), ("Realty", 57.5, -0.4), ("Media", 52.0, -1.1))


def seed_market_data(session: Session) -> MarketSnapshot:
    repository = MarketRepository(session)
    snapshot = repository.create_snapshot(MarketSnapshot(snapshot_time=datetime.now(timezone.utc), market_status="OPEN", market_regime="BULL", market_health_score=78.5, advance_decline_ratio=1.42, volatility_index=13.8, breadth_score=74.0))
    for rank, (name, strength, momentum) in enumerate(SECTORS, start=1):
        repository.create_sector_strength(SectorStrength(snapshot_id=snapshot.id, sector_name=name, rank=rank, strength_score=strength, momentum_score=momentum))
    repository.create_market_regime(MarketRegime(snapshot_id=snapshot.id, regime="BULL", confidence=82.0, reason="Mock seed data: positive breadth and stable volatility."))
    session.commit()
    return snapshot
