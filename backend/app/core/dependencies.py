"""
=========================================================
File: dependencies.py

Purpose:
    Contains reusable FastAPI dependencies.

These dependencies will be used by protected APIs
to authenticate and authorize users.
=========================================================
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.security import decode_access_token

# ==========================================================
# OAuth2 Bearer Token
# ==========================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)

# ==========================================================
# Get Current User
# ==========================================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    """
    Validate JWT token and return payload.
    """

    try:
        payload = decode_access_token(token)

        return payload

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token.",
        ) from exc


# ==========================================================
# Get Current Admin
# ==========================================================

def get_current_admin(
    current_user=Depends(get_current_user),
):
    """
    Ensure current user has admin role.
    """

    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required.",
        )

    return current_user