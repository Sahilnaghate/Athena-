from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.market.models import MarketRegime, MarketSnapshot, SectorStrength


class MarketRepository:
    """Persistence boundary for the market schema."""

    def __init__(self, session: Session):
        self._session = session

    def create_snapshot(self, snapshot: MarketSnapshot) -> MarketSnapshot:
        self._session.add(snapshot)
        self._session.flush()
        return snapshot

    def get_latest_snapshot(self) -> MarketSnapshot | None:
        return self._session.scalar(select(MarketSnapshot).order_by(MarketSnapshot.snapshot_time.desc()))

    def list_snapshots(self) -> list[MarketSnapshot]:
        return list(self._session.scalars(select(MarketSnapshot).order_by(MarketSnapshot.snapshot_time.desc())))

    def create_sector_strength(self, sector: SectorStrength) -> SectorStrength:
        self._session.add(sector)
        self._session.flush()
        return sector

    def get_sector_strength(self, snapshot_id: UUID) -> list[SectorStrength]:
        return list(self._session.scalars(select(SectorStrength).where(SectorStrength.snapshot_id == snapshot_id).order_by(SectorStrength.rank)))

    def create_market_regime(self, regime: MarketRegime) -> MarketRegime:
        self._session.add(regime)
        self._session.flush()
        return regime

    def get_market_regime(self, snapshot_id: UUID) -> MarketRegime | None:
        return self._session.scalar(select(MarketRegime).where(MarketRegime.snapshot_id == snapshot_id).order_by(MarketRegime.created_at.desc()))
