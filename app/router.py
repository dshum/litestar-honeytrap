from typing import Any

from advanced_alchemy.filters import LimitOffset
from litestar import post, get
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.response import Template
from litestar_htmx import ClientRefresh, HTMXTemplate
from sqlalchemy.ext.asyncio import AsyncSession

from app.forms import FeedbackForm
from app.models import MessageService


@get("/")
async def index(db_session: AsyncSession) -> Template:
    return Template(template_name="index.html")


@get("/form")
async def show_form() -> HTMXTemplate:
    form = FeedbackForm()
    return HTMXTemplate(template_name="form.html", context={"form": form})


@post("/form")
async def post_form(
        message_service: MessageService,
        data: dict[str, Any] = Body(media_type=RequestEncodingType.URL_ENCODED),
) -> HTMXTemplate | ClientRefresh:
    form = FeedbackForm(data=data)
    if form.validate():
        await message_service.create(form.data)
        return ClientRefresh()
    return HTMXTemplate(template_name="form.html", context={"form": form})


@get("/messages")
async def show_messages(
        message_service: MessageService,
        limit_offset: LimitOffset,
) -> HTMXTemplate:
    messages, count = await message_service.list_and_count(limit_offset)
    next_offset = limit_offset.offset + limit_offset.limit \
        if count > limit_offset.offset + limit_offset.limit \
        else None
    return HTMXTemplate(template_name="messages.html", context={
        "messages": messages,
        "offset": limit_offset.offset,
        "next_offset": next_offset,
    })
