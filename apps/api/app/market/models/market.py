from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Index, Numeric, String, func
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class MarketSnapshot(Base):
    __tablename__ = "market_snapshot"
    __table_args__ = (Index("ix_market_snapshot_snapshot_time", "snapshot_time"), Index("ix_market_snapshot_market_regime", "market_regime"), {"schema": "market"})

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    snapshot_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    market_status: Mapped[str] = mapped_column(String(20), nullable=False)
    market_regime: Mapped[str] = mapped_column(String(20), nullable=False)
    market_health_score: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    advance_decline_ratio: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    volatility_index: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    breadth_score: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    sectors: Mapped[list["SectorStrength"]] = relationship(back_populates="snapshot", cascade="all, delete-orphan")
    regimes: Mapped[list["MarketRegime"]] = relationship(back_populates="snapshot", cascade="all, delete-orphan")


class SectorStrength(Base):
    __tablename__ = "sector_strength"
    __table_args__ = {"schema": "market"}

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    snapshot_id: Mapped[UUID] = mapped_column(ForeignKey("market.market_snapshot.id"), nullable=False, index=True)
    sector_name: Mapped[str] = mapped_column(String(100), nullable=False)
    rank: Mapped[int] = mapped_column(nullable=False)
    strength_score: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    momentum_score: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    snapshot: Mapped[MarketSnapshot] = relationship(back_populates="sectors")


class MarketRegime(Base):
    __tablename__ = "market_regime"
    __table_args__ = {"schema": "market"}

    id: Mapped[UUID] = mapped_column(PostgreSQLUUID(as_uuid=True), primary_key=True, default=uuid4)
    snapshot_id: Mapped[UUID] = mapped_column(ForeignKey("market.market_snapshot.id"), nullable=False, index=True)
    regime: Mapped[str] = mapped_column(String(20), nullable=False)
    confidence: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    reason: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    snapshot: Mapped[MarketSnapshot] = relationship(back_populates="regimes")
