from sqlalchemy.orm import Session

from app.models.job_description import JobDescription


class JobRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        job: JobDescription,
    ):

        self.db.add(job)

        self.db.commit()

        self.db.refresh(job)

        return job

    def get_by_id(
        self,
        job_id: str,
    ):

        return (
            self.db.query(
                JobDescription,
            )
            .filter(
                JobDescription.id == job_id,
            )
            .first()
        )