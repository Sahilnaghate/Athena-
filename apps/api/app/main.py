from contextlib import asynccontextmanager

import redis.asyncio as redis
from fastapi import FastAPI
from sqlalchemy import text

from app.config import get_settings
from app.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.state.redis = redis.from_url(str(settings.redis_url), decode_responses=True)
    yield
    await app.state.redis.aclose()


app = FastAPI(title="ATHENA API", version="0.1.0", lifespan=lifespan)


@app.get("/health", tags=["platform"])
async def health() -> dict[str, str]:
    """Verify the platform's API, database, and Redis dependencies."""
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    await app.state.redis.ping()
    return {"status": "ok", "database": "ok", "redis": "ok"}

