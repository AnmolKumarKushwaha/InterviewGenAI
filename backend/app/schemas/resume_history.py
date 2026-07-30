from datetime import datetime

from pydantic import BaseModel


class ResumeHistoryResponse(BaseModel):

    id: str

    original_filename: str

    created_at: datetime

    resume_score: int | None

    class Config:

        from_attributes = True