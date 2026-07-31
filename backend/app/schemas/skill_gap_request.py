from uuid import UUID

from pydantic import BaseModel


class SkillGapRequest(BaseModel):

    resume_id: UUID

    job_id: UUID