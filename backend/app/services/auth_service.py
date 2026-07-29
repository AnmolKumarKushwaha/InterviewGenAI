"""
=========================================================
File: auth_service.py

Purpose:
    Handles all authentication business logic.

=========================================================
"""

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.hashing import hash_password
from app.security.hashing import verify_password
from app.security.jwt import create_access_token


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
        user_data: UserCreate,
    ):

        existing_user = self.user_repository.get_by_email(
            user_data.email,
        )

        if existing_user:

            raise ValueError(
                "Email already registered."
            )

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hash_password(
                user_data.password,
            ),
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

        user = self.user_repository.get_by_email(
            email,
        )

        if user is None:

            raise ValueError(
                "Invalid email or password."
            )

        if not verify_password(
            password,
            user.hashed_password,
        ):

            raise ValueError(
                "Invalid email or password."
            )

        access_token = create_access_token(
            {
                "sub": user.email,
                "user_id": str(user.id),
            }
        )

        return access_token