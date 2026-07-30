from sqlalchemy.orm import Session

from app.models.resume import Resume


class ResumeRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        resume: Resume,
    ) -> Resume:

        self.db.add(resume)

        self.db.commit()

        self.db.refresh(resume)

        return resume

    def get_by_id(
        self,
        resume_id: str,
    ):

        return (
            self.db.query(Resume)
            .filter(
                Resume.id == resume_id,
            )
            .first()
        )

    def get_user_resumes(
        self,
        user_id: int,
    ):

        return (
            self.db.query(Resume)
            .filter(
                Resume.user_id == user_id,
            )
            .order_by(
                Resume.created_at.desc(),
            )
            .all()
        )
        
    def update_text(
        self,
        resume: Resume,
        text: str,
    ):

        resume.extracted_text = text

        self.db.commit()

        self.db.refresh(resume)

        return resume
    