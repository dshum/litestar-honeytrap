import asyncio

import pytest
from click.testing import CliRunner

from app.commands import messages_group

pytestmark = pytest.mark.anyio


async def test_messages(cli_runner: CliRunner):
    result = cli_runner.invoke(messages_group)
    assert result.exit_code == 0


async def test_create_messages(cli_runner: CliRunner):
    def _test_create_messages():
        return cli_runner.invoke(messages_group, ["create", "--count=10"])

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, _test_create_messages)

    assert "Created 10 messages" in result.stdout
    assert result.exit_code == 0


async def test_flush_messages(cli_runner: CliRunner):
    def _test_flush_messages():
        return cli_runner.invoke(messages_group, ["flush"])

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, _test_flush_messages)

    assert "Deleted all messages" in result.stdout
    assert result.exit_code == 0
