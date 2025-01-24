from typing import Any

import pytest
from httpx import AsyncClient
from litestar.status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

pytestmark = pytest.mark.anyio


async def test_index(test_client: AsyncClient):
    response = await test_client.get("/")
    assert response.status_code == HTTP_200_OK


async def test_form(test_client: AsyncClient):
    response = await test_client.get("/form")
    assert response.status_code == HTTP_200_OK


async def test_post_form_empty(test_client: AsyncClient):
    response = await test_client.post("/form")
    assert response.status_code == HTTP_200_OK


async def test_post_valid_form(
        test_client: AsyncClient,
        feedback_form_data: dict[str, Any],
):
    response = await test_client.post("/form", data=feedback_form_data)
    assert response.status_code == HTTP_201_CREATED
    assert response.headers.get("hx-refresh") == "true"


async def test_post_form_with_invalid_email(
        test_client: AsyncClient,
        feedback_form_data: dict[str, Any],
):
    feedback_form_data.update(email="invalid-email")
    response = await test_client.post("/form", data=feedback_form_data)
    assert response.status_code == HTTP_200_OK


async def test_empty_messages(test_client: AsyncClient):
    response = await test_client.get("/messages")
    assert response.status_code == HTTP_200_OK
    assert "No messages yet" in response.text


async def test_messages_with_invalid_offset_limit(test_client: AsyncClient):
    response = await test_client.get("/messages", params={"offset": -10, "limit": -10})
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert "Error 400" in response.text


async def test_create_and_list_messages(
        test_client: AsyncClient,
        feedback_form_data: dict[str, Any],
):
    # add a message
    response = await test_client.post("/form", data=feedback_form_data)
    assert response.status_code == HTTP_201_CREATED
    # the message must appear on /messages
    response = await test_client.get("/messages", params={"offset": 0, "limit": 10})
    assert feedback_form_data.get("message") in response.text


async def test_create_20_messages_and_paginate(
        test_client: AsyncClient,
        feedback_form_data: dict[str, Any],
):
    # add 20 messages
    for _ in range(20):
        response = await test_client.post("/form", data=feedback_form_data)
        assert response.status_code == HTTP_201_CREATED
    # show Next messages on /messages?offset=0
    response = await test_client.get("/messages", params={"offset": 0})
    assert "Next messages" in response.text
    assert "/messages?offset=10" in response.text
    # don't show Next messages on /messages?offset=10
    response = await test_client.get("/messages", params={"offset": 10})
    assert "Next messages" not in response.text
    # empty response on /messages?offset=20
    response = await test_client.get("/messages", params={"offset": 20})
    assert response.text == ""
