from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def get_token():

    response = client.post(
        "/v1/auth/token",
        json={
            "username": "admin",
            "password": "password"
        }
    )

    return response.json()["access_token"]


def test_completions_success():

    token = get_token()

    app.state.completion_response = {
        "message": "mock response"
    }

    response = client.post(
        "/v1/completions",
        headers={
            "Authorization":
                f"Bearer {token}"
        },
        json={
            "request_id": "req_123",
            "task": "test task",
            "models": {},
            "pipeline": {},
            "deployment": {}
        }
    )

    assert response.status_code == 200


def test_invalid_request_body():

    token = get_token()

    app.state.completion_response = {
        "message": "mock response"
    }

    response = client.post(
        "/v1/completions",
        headers={
            "Authorization":
                f"Bearer {token}"
        },
        json={}
    )

    assert response.status_code == 422