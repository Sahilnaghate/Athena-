from app.main import app


def test_application_metadata() -> None:
    assert app.title == "ATHENA API"

