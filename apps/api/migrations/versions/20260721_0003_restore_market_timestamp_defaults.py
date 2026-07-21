"""restore timestamp defaults after legacy Market schema upgrade

Revision ID: 20260721_0003
Revises: 20260721_0002
Create Date: 2026-07-21
"""

from alembic import op
import sqlalchemy as sa


revision = "20260721_0003"
down_revision = "20260721_0002"
branch_labels = None
depends_on = None


TIMESTAMP_COLUMNS = (
    ("market_snapshot", "created_at"),
    ("market_snapshot", "updated_at"),
    ("sector_strength", "created_at"),
    ("market_regime", "created_at"),
)


def upgrade() -> None:
    for table_name, column_name in TIMESTAMP_COLUMNS:
        op.alter_column(table_name, column_name, schema="market", server_default=sa.text("now()"))


def downgrade() -> None:
    for table_name, column_name in TIMESTAMP_COLUMNS:
        op.alter_column(table_name, column_name, schema="market", server_default=None)
