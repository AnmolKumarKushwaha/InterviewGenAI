from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import InvalidCredentialsException
from app.core.exceptions import UnauthorizedException
from app.core.exceptions import UserAlreadyExistsException
from app.core.exceptions import UserNotFoundException


def register_exception_handlers(
    app: FastAPI,
):

    @app.exception_handler(
        UserAlreadyExistsException,
    )
    async def user_exists_handler(
        request: Request,
        exc: UserAlreadyExistsException,
    ):

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        InvalidCredentialsException,
    )
    async def invalid_credentials_handler(
        request: Request,
        exc: InvalidCredentialsException,
    ):

        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        UserNotFoundException,
    )
    async def user_not_found_handler(
        request: Request,
        exc: UserNotFoundException,
    ):

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(
        UnauthorizedException,
    )
    async def unauthorized_handler(
        request: Request,
        exc: UnauthorizedException,
    ):

        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": str(exc),
            },
        )