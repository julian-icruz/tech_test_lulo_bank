import httpx
import pytest
from unittest.mock import AsyncMock, MagicMock


@pytest.mark.asyncio
async def test_extract_schedule_success(tvmaze_api_adapter):
    """
    Test that extract_schedule returns the expected list of dictionaries
    when the HTTP response is successful.
    """
    mock_response = [{"show": {"name": "Test Show", "id": 1}}]
    mock_httpx_response = MagicMock(spec=httpx.Response)
    mock_httpx_response.status_code = 200
    mock_httpx_response.json.return_value = mock_response
    mock_httpx_response.raise_for_status = AsyncMock()
    tvmaze_api_adapter.client.get = AsyncMock(return_value=mock_httpx_response)
    response = await tvmaze_api_adapter.extract_schedule("2024-01-01")
    assert response == mock_response


@pytest.mark.asyncio
async def test_extract_schedule_http_error(tvmaze_api_adapter):
    """
    Test that extract_schedule raises an exception when the HTTP status code is 404.
    """
    mock_httpx_response = MagicMock(spec=httpx.Response)
    mock_httpx_response.status_code = 404
    mock_httpx_response.raise_for_status = MagicMock(
        side_effect=httpx.HTTPStatusError(
            "404 Client Error", request=MagicMock(), response=mock_httpx_response
        )
    )
    tvmaze_api_adapter.client.get = AsyncMock(return_value=mock_httpx_response)
    with pytest.raises(Exception, match="404 Client Error"):
        await tvmaze_api_adapter.extract_schedule("2024-01-01")


@pytest.mark.asyncio
async def test_extract_schedule_request_error(tvmaze_api_adapter):
    """
    Test that extract_schedule raises an exception when a RequestError occurs.
    """
    tvmaze_api_adapter.client.get = AsyncMock(side_effect=httpx.RequestError("Timeout"))
    with pytest.raises(Exception, match="Request error occurred"):
        await tvmaze_api_adapter.extract_schedule("2024-01-01")


@pytest.mark.asyncio
async def test_extract_schedule_empty_response(tvmaze_api_adapter):
    """
    Test that extract_schedule returns an empty list when the API returns an empty response.
    """
    mock_httpx_response = MagicMock(spec=httpx.Response)
    mock_httpx_response.status_code = 200
    mock_httpx_response.json.return_value = []
    mock_httpx_response.raise_for_status = AsyncMock()
    tvmaze_api_adapter.client.get = AsyncMock(return_value=mock_httpx_response)
    response = await tvmaze_api_adapter.extract_schedule("2024-01-01")
    assert response == []
