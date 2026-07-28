"""
=========================================================
File: auth_service.py

Purpose:
    Contains authentication business logic.
=========================================================
"""

from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User

from app.repositories.user_repository import UserRepository

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    verify_refresh_token,
)


class AuthService:


    def __init__(
        self,
        db: Session,
    ):

        self.user_repository = UserRepository(db)



    # =====================================================
    # Register User
    # =====================================================

    def register_user(
        self,
        full_name: str,
        username: str,
        email: str,
        password: str,
    ):


        existing_email = (
            self.user_repository
            .get_by_email(email)
        )


        if existing_email:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )



        existing_username = (
            self.user_repository
            .get_by_username(username)
        )


        if existing_username:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken",
            )



        user = User(

            full_name=full_name,

            username=username,

            email=email,

            hashed_password=hash_password(password),

            role="user",

            is_active=True,

            is_verified=False,
        )



        return self.user_repository.create(user)



    # =====================================================
    # Login User
    # =====================================================

    def login_user(
        self,
        email: str,
        password: str,
    ):


        user = (
            self.user_repository
            .get_by_email(email)
        )



        if not user:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )



        password_valid = verify_password(
            password,
            user.hashed_password,
        )



        if not password_valid:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )



        # Update last login

        user.last_login = datetime.now(
            timezone.utc
        )


        self.user_repository.update(user)



        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )


        refresh_token = create_refresh_token(
            {
                "sub": str(user.id)
            }
        )



        return {

            "access_token": access_token,

            "refresh_token": refresh_token,

            "token_type": "bearer",
        }



    # =====================================================
    # Refresh Token
    # =====================================================

    def refresh_access_token(
        self,
        refresh_token: str,
    ):


        payload = verify_refresh_token(
            refresh_token
        )


        user_id = payload.get(
            "sub"
        )



        if not user_id:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )



        access_token = create_access_token(
            {
                "sub": user_id
            }
        )



        return {

            "access_token": access_token,

            "token_type": "bearer",
        }