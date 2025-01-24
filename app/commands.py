from typing import cast

import anyio
import click
from faker import Faker
from sqlalchemy import delete


@click.group(name="messages", help="Manage feedback messages.")
def messages_group() -> None:
    """Manage feedback messages."""


@messages_group.command(name="flush", help="Flush all messages")
def flush_messages() -> None:
    from app.configs import sqlalchemy_config
    from app.models import Message

    async def _flush_messages():
        async with sqlalchemy_config.get_session() as db_session:
            await db_session.execute(delete(Message))
            await db_session.commit()
            click.echo(f"Deleted all messages")

    anyio.run(_flush_messages)


@messages_group.command(name="create", help="Create messages")
@click.option(
    "--count",
    help="Amount of messages to create",
    type=click.INT,
    required=False,
    default=100,
)
def create_messages(count: int) -> None:
    from app.configs import sqlalchemy_config
    from app.models import Message, MessageService

    async def _create_messages(messages_count: int) -> None:
        fake = Faker()
        messages = []
        for _ in range(messages_count):
            message = Message(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                message=fake.text(),
                is_human=fake.boolean(),
            )
            messages.append(message)

        async with sqlalchemy_config.get_session() as db_session:
            message_service = MessageService(db_session)
            await message_service.create_many(data=messages, auto_commit=True)
            click.echo(f"Created {messages_count} messages")

    anyio.run(_create_messages, cast("int", count))
