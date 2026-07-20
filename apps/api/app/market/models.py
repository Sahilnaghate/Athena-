from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class MarketRegime(Base):
    __tablename__ = "market_regime"
    __table_args__ = {"schema": "market"}

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    regime: Mapped[str] = mapped_column(String(20), index=True)
    health_score: Mapped[float] = mapped_column(Numeric(5, 2))
    detected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class MarketSnapshot(Base):
    __tablename__ = "market_snapshot"
    __table_args__ = {"schema": "market"}

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    regime_id: Mapped[UUID] = mapped_column(ForeignKey("market.market_regime.id"), index=True)
    nifty50: Mapped[float] = mapped_column(Numeric(12, 2))
    sensex: Mapped[float] = mapped_column(Numeric(12, 2))
    bank_nifty: Mapped[float] = mapped_column(Numeric(12, 2))
    india_vix: Mapped[float] = mapped_column(Numeric(8, 2))
    advance_decline_ratio: Mapped[float] = mapped_column(Numeric(8, 2))
    captured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), index=True)


class SectorStrength(Base):
    __tablename__ = "sector_strength"
    __table_args__ = {"schema": "market"}

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    snapshot_id: Mapped[UUID] = mapped_column(ForeignKey("market.market_snapshot.id"), index=True)
    sector_name: Mapped[str] = mapped_column(String(100), index=True)
    rank: Mapped[int] = mapped_column(Integer, index=True)
    relative_strength: Mapped[float] = mapped_column(Numeric(8, 2))
    momentum: Mapped[float] = mapped_column(Numeric(8, 2))
    trend: Mapped[str] = mapped_column(String(20))
