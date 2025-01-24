from advanced_alchemy.filters import LimitOffset
from litestar.params import Parameter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import MessageService, Message



async def provide_limit_offset_pagination(
        offset: int = Parameter(query="offset", ge=0, default=0, required=False),
        limit: int = Parameter(query="limit", ge=1, le=100, default=10, required=False),
) -> LimitOffset:
    return LimitOffset(limit, offset)


async def provide_message_service(db_session: AsyncSession) -> MessageService:
    statement = select(Message).order_by(Message.created_at.desc())
    return MessageService(session=db_session, statement=statement)
