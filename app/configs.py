from pathlib import Path

from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig
from litestar.config.compression import CompressionConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.logging import StructLoggingConfig, LoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogConfig
from litestar.template import TemplateConfig
from sqlalchemy.ext.asyncio import create_async_engine

from app import settings
from app.models import Base

engine = create_async_engine(
    url=settings.db.URL,
    echo=settings.db.ECHO,
)

sqlalchemy_config = SQLAlchemyAsyncConfig(
    create_all=True,
    metadata=Base.metadata,
    before_send_handler="autocommit",
    engine_instance=engine,
)

template_config = TemplateConfig(
    directory=Path(__file__).parent / "templates",
    engine=JinjaTemplateEngine,
)

log_config = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="debug",
        standard_lib_logging_config=LoggingConfig(
            root={
                "level": settings.log.LEVEL,
                "handlers": ["queue_listener"],
            },
            loggers={
                "sqlalchemy.engine": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.pool": {
                    "propagate": False,
                    "level": settings.log.SQLALCHEMY_LEVEL,
                    "handlers": ["queue_listener"],
                },
            },
        ),
    ),
    middleware_logging_config=LoggingMiddlewareConfig(
        request_log_fields=["method", "path", "path_params", "query"],
        response_log_fields=["status_code"],
    ),
)

compression_config = CompressionConfig(
    backend="gzip",
    gzip_compress_level=9,
)
