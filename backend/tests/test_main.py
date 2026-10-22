
from fastapi.testclient import TestClient

from app.main import app
from app.core.config import Settings
from sqlalchemy import text
from app.db.database import SessionLocal

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to AI Interview Coach!"


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_settings_reads_environment_variable(monkeypatch):
    monkeypatch.setenv("APP_NAME", "Interview Coach Test")

    test_settings = Settings()

    assert test_settings.app_name == "Interview Coach Test"

def test_database_connection():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1")).scalar()
        assert result == 1
    finally:
        db.close()
