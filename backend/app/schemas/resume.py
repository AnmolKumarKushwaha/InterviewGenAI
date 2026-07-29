from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class ResumeResponse(BaseModel):

    id: str
    user_id: int

    original_filename: str
    stored_filename: str
    file_path: str

    file_size: int
    mime_type: str

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )