import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import httpx
from litestar import Litestar
from litestar.channels import ChannelsPlugin
from litestar.channels.backends.memory import MemoryChannelsBackend
from litestar.stores.memory import MemoryStore

store = MemoryStore()

channels = ChannelsPlugin(
    backend=MemoryChannelsBackend(),
    channels=["random-quote"],
    create_ws_route_handlers=True,
)


async def get_quote():
    quote = await store.get("random-quote")
    if not quote:
        response = httpx.get(
            url="https://api.api-ninjas.com/v1/quotes",
            headers={'X-Api-Key': "API-KEY"},
        )
        quote = response.json()[0]
        await store.set("random-quote", quote, expires_in=60)
    return quote


async def background_task():
    while True:
        quote = await get_quote()
        channels.publish(quote, ["random-quote"])
        await asyncio.sleep(60)


@asynccontextmanager
async def background_task_context(app: Litestar) -> AsyncGenerator[None, None]:
    task = asyncio.create_task(background_task())
    try:
        yield
    finally:
        task.cancel()


app = Litestar(
    route_handlers=[],
    plugins=[channels],
    lifespan=[background_task_context],
)
