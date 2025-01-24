from litestar import Litestar


def create_app() -> Litestar:
    from pathlib import Path

    from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
    from litestar import Router
    from litestar.di import Provide
    from litestar.exceptions import HTTPException, NotFoundException, ValidationException
    from litestar_htmx import HTMXRequest
    from litestar.plugins.structlog import StructlogPlugin
    from litestar.static_files import create_static_files_router

    from app import settings
    from app.configs import (
        compression_config,
        log_config,
        sqlalchemy_config,
        template_config,
    )
    from app.dependencies import provide_limit_offset_pagination, provide_message_service
    from app.exceptions import (
        http_exception_handler,
        not_found_exception_handler,
        validation_exception_handler,
    )
    from app.plugins import CLIPlugin
    from app.router import index, show_form, post_form, show_messages

    feedback_router = Router(
        path="/",
        route_handlers=[index, show_form, post_form, show_messages],
        dependencies={
            "limit_offset": Provide(provide_limit_offset_pagination),
            "message_service": Provide(provide_message_service),
        },
    )

    return Litestar(
        route_handlers=[
            feedback_router,
            create_static_files_router(
                directories=[Path(__file__).resolve().parent / "static"],
                path="/static",
            ),
        ],
        plugins=[
            CLIPlugin(),
            SQLAlchemyPlugin(config=sqlalchemy_config),
            StructlogPlugin(config=log_config),
        ],
        request_class=HTMXRequest,
        template_config=template_config,
        compression_config=compression_config,
        exception_handlers={
            NotFoundException: not_found_exception_handler,
            ValidationException: validation_exception_handler,
            HTTPException: http_exception_handler,
        },
        debug=settings.app.DEBUG,
    )


app = create_app()
