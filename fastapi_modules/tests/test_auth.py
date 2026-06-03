from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_login_success():

    response = client.post(
        "/v1/auth/token",
        json={
            "username": "admin",
            "password": "password"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert "access_token" in body


def test_login_failure():

    response = client.post(
        "/v1/auth/token",
        json={
            "username": "wrong",
            "password": "wrong"
        }
    )

    assert response.status_code == 401


def test_completions_without_token():

    response = client.post(
        "/v1/completions",
        json={
            "request_id": "req_123",
            "task": "test task",
            "models": {},
            "pipeline": {},
            "deployment": {}
        }
    )

    assert response.status_code in [401, 403]