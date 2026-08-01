from pydantic import BaseModel

class SemanticMatch(

    BaseModel,
):

    resume_skill: str

    job_skill: str

    score: float
    
    
    
class LearningPriority(BaseModel):

    skill: str

    priority: str
    
    
class SkillExplanation(BaseModel):

    skill: str

    importance: str

    priority: str
    
    resource: str

    learning_time: str
    
    

class SkillGapResponse(BaseModel):

    match_percentage: float

    matched_skills: list[str]

    missing_skills: list[str]
    
    semantic_matches: list[SemanticMatch]
    
    matched_weight: int

    total_weight: int

    learning_recommendations: list[str]
    
    learning_priorities: list[LearningPriority]
    
    ai_feedback: str
    
    skill_explanations: list[SkillExplanation]
    
    learning_roadmap: dict

    class Config:

        from_attributes = True
        