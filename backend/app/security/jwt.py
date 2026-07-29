"""
=========================================================
File: jwt.py

Purpose:
    Creates and verifies JWT access tokens.

=========================================================
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import JWTError
from jose import jwt

from app.core.config import settings


# =========================================================
# Create Access Token
# =========================================================

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
) -> str:

    payload = data.copy()

    if expires_delta:

        expire = datetime.now(
            timezone.utc,
        ) + expires_delta

    else:

        expire = datetime.now(
            timezone.utc,
        ) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )

    payload.update(
        {
            "exp": expire,
        }
    )

    encoded_jwt = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt


# =========================================================
# Decode Token
# =========================================================

def decode_access_token(
    token: str,
):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        return payload

    except JWTError:

        return None