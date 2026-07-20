from sqlalchemy import select
from sqlalchemy.orm import Session

from app.market.models import MarketRegime, MarketSnapshot, SectorStrength
from app.market.provider import MarketData


class MarketRepository:
    def __init__(self, session: Session):
        self._session = session

    def store_snapshot(self, data: MarketData, regime: str, health_score: float) -> MarketSnapshot:
        record = MarketRegime(regime=regime, health_score=health_score)
        self._session.add(record)
        self._session.flush()
        snapshot = MarketSnapshot(
            regime_id=record.id, nifty50=data.nifty50, sensex=data.sensex, bank_nifty=data.bank_nifty,
            india_vix=data.india_vix, advance_decline_ratio=data.advance_decline_ratio,
        )
        self._session.add(snapshot)
        self._session.flush()
        for rank, sector in enumerate(sorted(data.sectors, key=lambda item: item.relative_strength, reverse=True), start=1):
            self._session.add(SectorStrength(snapshot_id=snapshot.id, sector_name=sector.name, rank=rank, relative_strength=sector.relative_strength, momentum=sector.momentum, trend="BULL" if sector.momentum > 0 else "BEAR"))
        self._session.commit()
        self._session.refresh(snapshot)
        return snapshot

    def latest_snapshot(self) -> MarketSnapshot | None:
        return self._session.scalar(select(MarketSnapshot).order_by(MarketSnapshot.captured_at.desc()))

    def latest_regime(self) -> MarketRegime | None:
        return self._session.scalar(select(MarketRegime).order_by(MarketRegime.detected_at.desc()))

    def sector_ranking(self, snapshot_id: object) -> list[SectorStrength]:
        return list(self._session.scalars(select(SectorStrength).where(SectorStrength.snapshot_id == snapshot_id).order_by(SectorStrength.rank)))
