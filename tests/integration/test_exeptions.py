import pytest
from httpx import AsyncClient
from litestar.status_codes import HTTP_404_NOT_FOUND

pytestmark = pytest.mark.anyio


async def test_not_found_error(test_client: AsyncClient):
    response = await test_client.get("/404")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert "Error 404" in response.text
