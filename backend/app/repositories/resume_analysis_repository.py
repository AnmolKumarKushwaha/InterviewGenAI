from sqlalchemy.orm import Session

from app.models.resume_analysis import ResumeAnalysis


class ResumeAnalysisRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        analysis: ResumeAnalysis,
    ):

        self.db.add(analysis)

        self.db.commit()

        self.db.refresh(analysis)

        return analysis
    
    
    def get_by_resume_id (
        self,
        resume_id: str,
    
    ):

        return (
             self.db.query(
                ResumeAnalysis,
            )
            .filter(
                ResumeAnalysis.resume_id == resume_id,
            )
            .first()
    )