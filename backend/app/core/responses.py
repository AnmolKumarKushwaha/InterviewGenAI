"""
=========================================================
File: responses.py

Purpose:
    Provides standardized API responses.

Every endpoint should return a consistent response
format across the application.
=========================================================
"""

from typing import Any

from fastapi.responses import JSONResponse


def success_response(
    message: str,
    data: Any = None,
    status_code: int = 200,
) -> JSONResponse:
    """
    Standard success response.
    """

    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data,
        },
    )


def error_response(
    message: str,
    error_code: str,
    status_code: int = 400,
) -> JSONResponse:
    """
    Standard error response.
    """

    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "error_code": error_code,
        },
    )