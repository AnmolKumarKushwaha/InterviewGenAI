from pydantic import BaseModel


class ResumeAnalysisResponse(BaseModel):
   
    resume_id: str
    
    resume_score: int
    
    extracted_skills: list

    extracted_projects: list

    extracted_experience: list

    extracted_education: list

    missing_skills: list

    suggestions: list

    class Config:

        from_attributes = True