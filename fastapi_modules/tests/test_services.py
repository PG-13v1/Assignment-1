import pytest

from services import fetch_json


@pytest.mark.asyncio
async def test_fetch_json_mock(mocker):

    response = mocker.Mock()

    response.json.return_value = {
        "status": "ok"
    }

    response.raise_for_status.return_value = None

    mock_get = mocker.AsyncMock(
        return_value=response
    )

    mocker.patch(
        "httpx.AsyncClient.get",
        mock_get
    )

    result = await fetch_json(
        "https://example.com"
    )

    assert result == {
        "status": "ok"
    }