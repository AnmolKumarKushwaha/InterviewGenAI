"""
=========================================================
File: auth.py

Purpose:
    Authentication API endpoints.

Endpoints:

    POST /register
    POST /login
    POST /refresh
    GET  /me

=========================================================
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
)

from app.schemas.auth import (
    LoginRequest,
    RefreshTokenRequest,
)

from app.schemas.token import Token
from app.schemas.token import (
    Token
)

from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies.auth import (
    get_current_user,
)

from app.models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# ==========================================================
# Register
# ==========================================================

@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):

    auth_service = AuthService(db)


    user = auth_service.register_user(
        full_name=user_data.full_name,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
    )


    return user



# ==========================================================
# Login
# ==========================================================

@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    auth_service = AuthService(db)


    tokens = auth_service.login_user(
        email=form_data.username,
        password=form_data.password,
    )


    return tokens

# ==========================================================
# Refresh Token
# ==========================================================

@router.post(
    "/refresh",
    response_model=Token,
)
def refresh_token(
    data: RefreshTokenRequest,
    db: Session = Depends(get_db),
):

    auth_service = AuthService(db)


    token = auth_service.refresh_access_token(
        data.refresh_token
    )


    return token



# ==========================================================
# Current User
# ==========================================================

@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(
        get_current_user
    ),
):

    return current_user