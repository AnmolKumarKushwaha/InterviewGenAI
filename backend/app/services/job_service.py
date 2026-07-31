from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.ai.job_analyzer import JobAnalyzer
from app.models.job_analysis import JobAnalysis
from app.models.job_description import JobDescription
from app.models.user import User

from app.repositories.job_analysis_repository import JobAnalysisRepository
from app.repositories.job_repository import JobRepository

from app.schemas.job import JobCreate


class JobService:

    def __init__(
        self,
        db: Session,
    ):

        self.repository = JobRepository(
            db,
        )

        self.analysis_repository = JobAnalysisRepository(
            db,
        )

    def create_job(
        self,
        data: JobCreate,
        current_user: User,
    ):

        job = JobDescription(

            user_id=current_user.id,

            title=data.title,

            description=data.description,
        )

        job = self.repository.create(
            job,
        )

        analysis = JobAnalyzer.analyze(
            data.description,
        )

        analysis_record = JobAnalysis(

            job_id=job.id,

            required_skills=analysis["required_skills"],

            preferred_skills=analysis["preferred_skills"],

            responsibilities=analysis["responsibilities"],

            experience=analysis["experience"],

            education=analysis["education"],

            location=analysis["location"],
        )

        self.analysis_repository.create(
            analysis_record,
        )

        return job

    def get_analysis(
        self,
        job_id: str,
    ):

        analysis = self.analysis_repository.get_by_job_id(
            job_id,
        )

        if analysis is None:

            raise HTTPException(
                status_code=404,
                detail="Analysis not found.",
            )

        return analysis