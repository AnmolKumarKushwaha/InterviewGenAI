"""
=========================================================
File: security.py

Purpose:
    Handles password hashing and JWT token management.

Used by:
    - Authentication
    - Authorization
    - Protected APIs
=========================================================
"""

from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from pwdlib import PasswordHash

from app.core.config import settings

# ==========================================================
# Password Hasher
# ==========================================================

password_hash = PasswordHash.recommended()

# ==========================================================
# Hash Password
# ==========================================================

def hash_password(password: str) -> str:
    """
    Hash a plain text password before storing it.
    """
    return password_hash.hash(password)


# ==========================================================
# Verify Password
# ==========================================================

def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Compare a plain password with its hashed version.
    """
    return password_hash.verify(plain_password, hashed_password)


# ==========================================================
# Create JWT Access Token
# ==========================================================

def create_access_token(subject: str) -> str:
    """
    Generate a JWT access token.
    """

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


# ==========================================================
# Decode JWT
# ==========================================================

def decode_access_token(token: str) -> dict:
    """
    Decode and validate a JWT token.
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        return payload

    except JWTError as exc:
        raise ValueError("Invalid or expired token.") from exc