"""Tests for the service and health endpoints."""

from app import create_app


def test_index():
    """The root route returns service metadata."""
    response = create_app().test_client().get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "devops-ci-app",
        "version": "1.0.0",
        "status": "running",
    }


def test_health():
    """The health route reports that the service is healthy."""
    response = create_app().test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
