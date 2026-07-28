"""
=========================================================
File: security.py

Purpose:
    Handles password hashing, password verification,
    JWT creation, JWT validation and OAuth2 configuration.

=========================================================
"""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

# ==========================================================
# Password Hashing
# ==========================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

# ==========================================================
# JWT Configuration
# ==========================================================

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = 7


def hash_password(password: str) -> str:
    """
    Returns hashed password.
    """

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verifies password.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(
    data: dict[str, Any],
) -> str:
    """
    Creates Access Token.
    """

    payload = data.copy()

    expire = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload.update(
        {
            "exp": expire,
            "type": "access",
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def create_refresh_token(
    data: dict[str, Any],
) -> str:
    """
    Creates Refresh Token.
    """

    payload = data.copy()

    expire = (
        datetime.now(timezone.utc)
        + timedelta(
            days=REFRESH_TOKEN_EXPIRE_DAYS
        )
    )

    payload.update(
        {
            "exp": expire,
            "type": "refresh",
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_token(
    token: str,
) -> dict[str, Any]:
    """
    Decodes JWT.
    """

    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )


def verify_access_token(
    token: str,
) -> dict[str, Any]:
    """
    Validates Access Token.
    """

    payload = decode_token(token)

    if payload.get("type") != "access":
        raise JWTError("Invalid Access Token")

    return payload


def verify_refresh_token(
    token: str,
) -> dict[str, Any]:
    """
    Validates Refresh Token.
    """

    payload = decode_token(token)

    if payload.get("type") != "refresh":
        raise JWTError("Invalid Refresh Token")

    return payload