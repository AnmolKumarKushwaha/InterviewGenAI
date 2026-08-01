from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.ai.skill_gap_analyzer import SkillGapAnalyzer

from app.models.skill_gap import SkillGap

from app.repositories.resume_analysis_repository import ResumeAnalysisRepository
from app.repositories.job_analysis_repository import JobAnalysisRepository
from app.repositories.skill_gap_repository import SkillGapRepository
from app.ai.explanation_generator import ExplanationGenerator
from app.ai.roadmap_generator import RoadmapGenerator
from app.ai.interview_generator import InterviewGenerator
from app.ai.career_report_generator import CareerReportGenerator

class SkillGapService:

    def __init__(
        self,
        db: Session,
    ):

        self.resume_repository = ResumeAnalysisRepository(
            db,
        )

        self.job_repository = JobAnalysisRepository(
            db,
        )

        self.repository = SkillGapRepository(
            db,
        )

    def analyze(
        self,
        resume_id: str,
        job_id: str,
    ):
        
        
        print("=" * 60)
        print("Resume ID:", resume_id)
        print("Job ID:", job_id)
        print("=" * 60)

        resume = self.resume_repository.get_by_resume_id(
            resume_id,
        )
        
        print("Resume Analysis:", resume)

        if resume is None:

            raise HTTPException(
                status_code=404,
                detail="Resume analysis not found.",
            )

        job = self.job_repository.get_by_job_id(
            job_id,
        )
        
        print("=" * 60)
        print("Job Analysis:", job)
        print("=" * 60)

        if job is None:

            raise HTTPException(
                status_code=404,
                detail="Job analysis not found.",
            )

        result = SkillGapAnalyzer.analyze(
            resume,
            job,
        )
        
        print("=" * 60)
        print(result)
        print("=" * 60)
        
        skill_explanations = ExplanationGenerator.generate(result["missing_skills"],)
        
        roadmap = RoadmapGenerator.generate(

            resume_skills=resume.extracted_skills,

            missing_skills=result["missing_skills"],

            learning_priorities=result["learning_priorities"],

            skill_explanations=skill_explanations,
        )
        
        interview_preparation = InterviewGenerator.generate(

            resume_skills=resume.extracted_skills,

            missing_skills=result["missing_skills"],

            learning_priorities=result["learning_priorities"],

            skill_explanations=skill_explanations,

            learning_roadmap=roadmap,
        )
        
        
        career_report = CareerReportGenerator.generate(

            resume_skills=resume.extracted_skills,

            missing_skills=result["missing_skills"],

            match_percentage=result["match_percentage"],

            learning_priorities=result["learning_priorities"],

            skill_explanations=skill_explanations,

            learning_roadmap=roadmap,

            interview_preparation=interview_preparation,
        )
        
        
        gap = SkillGap(

            resume_id=resume_id,

            job_id=job_id,

            match_percentage=result["match_percentage"],

            matched_skills=result["matched_skills"],

            missing_skills=result["missing_skills"],
            
            semantic_matches=result["semantic_matches"],
            
            matched_weight=result["matched_weight"],
            
            total_weight=result["total_weight"],

            learning_recommendations=result[
                "learning_recommendations"
            ],
            
            ai_feedback=result["ai_feedback"],
            
            learning_priorities=result["learning_priorities"],
            
            skill_explanations=skill_explanations,
            
            learning_roadmap=roadmap,
            
            interview_preparation=interview_preparation,
            
            career_report=career_report,
        )

        print("=" * 60)
        print("Analyzer Result:", result)
        print("Saving SkillGap...")
        print("=" * 60)
        
        saved = self.repository.create(gap)
        
        
        print("=" * 60)
        print("SkillGap Saved:", saved)
        print("=" * 60)

        print("Saved Successfully")
        return saved