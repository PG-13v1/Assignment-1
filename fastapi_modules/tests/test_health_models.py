from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_health_endpoint(mocker):

    mocker.patch(
        "api.v1.routes.fetch_json",
        return_value=[
            {
                "title": "healthy",
                "bite": "all good",
                "url": "/health"
            }
        ]
    )

    response = client.get(
        "/v1/health"
    )

    assert response.status_code == 200


def test_models_endpoint(mocker):

    mocker.patch(
        "api.v1.routes.fetch_json",
        return_value=[
            {"driver": "max"},
            {"driver": "lando"}
        ]
    )

    response = client.get(
        "/v1/models"
    )

    assert response.status_code == 200
