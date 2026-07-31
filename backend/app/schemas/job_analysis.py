from pydantic import BaseModel


class JobAnalysisResponse(BaseModel):

    required_skills: list[str]

    preferred_skills: list[str]

    responsibilities: list[str]

    experience: str | None

    education: str | None

    location: str | None

    class Config:

        from_attributes = True