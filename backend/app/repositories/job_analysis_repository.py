from sqlalchemy.orm import Session

from app.models.job_analysis import JobAnalysis


class JobAnalysisRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        analysis: JobAnalysis,
    ):

        self.db.add(
            analysis,
        )

        self.db.commit()

        self.db.refresh(
            analysis,
        )

        return analysis

    def get_by_job_id(
        self,
        job_id: str,
    ):

        return (
            self.db.query(
                JobAnalysis,
            )
            .filter(
                JobAnalysis.job_id == job_id,
            )
            .first()
        )