from typing import AsyncGenerator, AsyncIterator

import pytest
from click.testing import CliRunner
from litestar import Litestar
from litestar.testing import AsyncTestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession

from app.configs import sqlalchemy_config
from app.models import Base

pytestmark = pytest.mark.anyio


@pytest.fixture(name="engine")
async def fx_engine() -> AsyncEngine:
    return create_async_engine("sqlite+aiosqlite:///:memory:")


@pytest.fixture(name="sessionmaker")
def fx_sessionmaker(engine: AsyncEngine) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
    yield async_sessionmaker(bind=engine, expire_on_commit=False)


@pytest.fixture(name="session")
async def fx_session(sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
    async with sessionmaker() as session:
        yield session


@pytest.fixture(autouse=True)
def _patch_db(
        engine: AsyncEngine,
        sessionmaker: async_sessionmaker[AsyncSession],
        monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(sqlalchemy_config, "session_maker", sessionmaker)
    monkeypatch.setattr(sqlalchemy_config, "engine_instance", engine)


@pytest.fixture(autouse=True)
async def _seed_db(engine: AsyncEngine) -> AsyncGenerator[None, None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest.fixture()
def anyio_backend():
    return "asyncio"


@pytest.fixture()
def app() -> Litestar:
    from app.main import create_app
    return create_app()


@pytest.fixture()
async def test_client(app: Litestar) -> AsyncIterator[AsyncTestClient[Litestar]]:
    async with AsyncTestClient(app=app) as client:
        yield client


@pytest.fixture()
def cli_runner() -> CliRunner:
    return CliRunner()
