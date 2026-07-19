import asyncio
import json
import logging
import os
import signal
from datetime import datetime, timezone

import redis.asyncio as redis


class JsonFormatter(logging.Formatter):
    """Emit consistent machine-readable worker logs."""

    def format(self, record: logging.LogRecord) -> str:
        return json.dumps(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "level": record.levelname.lower(),
                "service": "worker",
                "requestId": None,
                "correlationId": None,
                "message": record.getMessage(),
            }
        )


def configure_logging() -> logging.Logger:
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logger = logging.getLogger("athena.worker")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.propagate = False
    return logger


async def run_worker() -> None:
    """Keep the worker process available for future queue-backed jobs."""
    logger = configure_logging()
    shutdown = asyncio.Event()
    loop = asyncio.get_running_loop()

    for signal_name in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(signal_name, shutdown.set)

    client = redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/0"))
    try:
        await client.ping()
        logger.info("ATHENA worker started")

        while not shutdown.is_set():
            try:
                await asyncio.wait_for(shutdown.wait(), timeout=30)
            except TimeoutError:
                await client.ping()
                logger.info("Worker heartbeat")
    finally:
        await client.aclose()
        logger.info("ATHENA worker stopped")


def main() -> None:
    asyncio.run(run_worker())


if __name__ == "__main__":
    main()
