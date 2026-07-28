from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):

    full_name: str

    username: str

    email: EmailStr

    password: str


class UserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    full_name: str

    username: str

    email: EmailStr

    role: str

    is_active: bool

    is_verified: bool