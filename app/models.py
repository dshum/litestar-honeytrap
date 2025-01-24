from advanced_alchemy.base import UUIDAuditBase, UUIDBase
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped


class Base(UUIDBase):
    ...


class Message(UUIDAuditBase):
    __tablename__ = "messages"
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    message: Mapped[str]
    is_human: Mapped[bool]

    @hybrid_property
    def author(self):
        return "{} {}".format(self.first_name, self.last_name)


class MessageRepository(SQLAlchemyAsyncRepository[Message]):
    model_type = Message


class MessageService(SQLAlchemyAsyncRepositoryService[Message]):
    repository_type = MessageRepository
