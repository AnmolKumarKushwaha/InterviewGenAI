from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class JobResponse(BaseModel):

    id: UUID

    title: str

    description: str

    created_at: datetime

    class Config:

        from_attributes = True