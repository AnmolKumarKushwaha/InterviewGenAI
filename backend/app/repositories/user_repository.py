from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(self, db: Session):

        self.db = db

    def get_by_email(self, email: str):

        return self.db.scalar(
            select(User).where(User.email == email)
        )

    def get_by_username(self, username: str):

        return self.db.scalar(
            select(User).where(User.username == username)
        )

    def create(self, user: User):

        self.db.add(user)

        self.db.commit()

        self.db.refresh(user)

        return user
    
    def update(
        self,
        user: User
    ):

        self.db.commit()

        self.db.refresh(user)

        return user