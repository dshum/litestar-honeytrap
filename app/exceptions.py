from litestar import Request
from litestar.exceptions import HTTPException, NotFoundException, ValidationException
from litestar.response import Template


def http_exception_handler(request: Request, exc: HTTPException) -> Template:
    return Template("error.html", context={"code": 500}, status_code=500)


def not_found_exception_handler(request: Request, exc: NotFoundException) -> Template:
    return Template("error.html", context={"code": 404}, status_code=404)


def validation_exception_handler(request: Request, exc: ValidationException) -> Template:
    return Template("error.html", context={"code": 400}, status_code=400)
