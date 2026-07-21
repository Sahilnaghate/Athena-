from contextlib import asynccontextmanager
import time
from uuid import uuid4

import redis.asyncio as redis
from fastapi import FastAPI, Request, Response
from sqlalchemy import text

from app.config import get_settings
from app.database import engine
from app.logging import configure_logging
from app.market.router import router as market_router

logger = configure_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.state.redis = redis.from_url(str(settings.redis_url), decode_responses=True)
    yield
    await app.state.redis.aclose()


app = FastAPI(title="ATHENA API", version="0.1.0", lifespan=lifespan)
app.include_router(market_router)


@app.middleware("http")
async def log_request(request: Request, call_next) -> Response:
    request_id = request.headers.get("x-request-id", str(uuid4()))
    correlation_id = request.headers.get("x-correlation-id", request_id)
    request.state.request_id = request_id
    request.state.correlation_id = correlation_id
    started_at = time.perf_counter()
    response = await call_next(request)
    duration_ms = round((time.perf_counter() - started_at) * 1000, 2)
    response.headers["x-request-id"] = request_id
    response.headers["x-correlation-id"] = correlation_id
    logger.info(
        "Request completed",
        extra={
            "request_id": request_id,
            "correlation_id": correlation_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
        },
    )
    return response


@app.get("/health", tags=["platform"])
async def health(request: Request) -> dict[str, str]:
    """Verify the platform's API, database, and Redis dependencies."""
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    await app.state.redis.ping()
    logger.info(
        "Health check completed",
        extra={
            "request_id": request.state.request_id,
            "correlation_id": request.state.correlation_id,
        },
    )
    return {"status": "ok", "database": "ok", "redis": "ok"}
