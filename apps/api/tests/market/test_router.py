from datetime import datetime, timezone
from unittest.mock import MagicMock
from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app
from app.market.dependencies import get_market_service
from app.market.models import MarketSnapshot
from app.market.service import MarketPersistenceError


def snapshot() -> MarketSnapshot:
    return MarketSnapshot(id=uuid4(), snapshot_time=datetime.now(timezone.utc), market_status="OPEN", market_regime="BULL", market_health_score=78, advance_decline_ratio=1.4, volatility_index=14, breadth_score=71)


def client_with(service: MagicMock) -> TestClient:
    app.dependency_overrides[get_market_service] = lambda: service
    return TestClient(app)


def test_refresh_endpoint_calls_service() -> None:
    service = MagicMock()
    service.refresh_market.return_value = snapshot()
    service.get_snapshot_regime.return_value = None
    response = client_with(service).post("/api/v1/market/refresh")
    assert response.status_code == 200
    service.refresh_market.assert_called_once()


def test_latest_endpoint_returns_snapshot() -> None:
    service = MagicMock()
    service.get_latest_market_state.return_value = (snapshot(), None, [])
    response = client_with(service).get("/api/v1/market/latest")
    assert response.status_code == 200
    assert response.json()["data"]["snapshot"]["market_regime"] == "BULL"


def test_latest_endpoint_returns_not_found_without_snapshot() -> None:
    service = MagicMock()
    service.get_latest_market_state.return_value = None
    assert client_with(service).get("/api/v1/market/latest").status_code == 404


def test_history_endpoint_paginates_snapshots() -> None:
    service = MagicMock()
    service.list_market_history.return_value = [snapshot(), snapshot(), snapshot()]
    service.get_snapshot_regime.return_value = None
    response = client_with(service).get("/api/v1/market/history?page=2&page_size=2")
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_refresh_endpoint_hides_service_errors() -> None:
    service = MagicMock()
    service.refresh_market.side_effect = MarketPersistenceError("database unavailable")
    response = client_with(service).post("/api/v1/market/refresh")
    assert response.status_code == 500
    assert response.json()["detail"] == "Market refresh failed"


def test_latest_openapi_schema_is_typed() -> None:
    schema = TestClient(app).get("/openapi.json").json()
    latest_response = schema["paths"]["/api/v1/market/latest"]["get"]["responses"]["200"]["content"]["application/json"]["schema"]

    assert latest_response["$ref"].endswith("/MarketLatestResponse")
    assert schema["components"]["schemas"]["MarketLatestResponse"]["properties"]["data"]["$ref"].endswith("/CurrentMarketStateResponse")
