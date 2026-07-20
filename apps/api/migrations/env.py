from alembic import context
from sqlalchemy import engine_from_config, pool

from app.database import Base
from app.market import models  # noqa: F401

config = context.config


def run_migrations_online() -> None:
    connectable = engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata, include_schemas=True)
        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
