from sentence_transformers import SentenceTransformer

from app.utils.similarity import cosine_similarity


class SemanticMatcher:

    model = SentenceTransformer(

        "all-MiniLM-L6-v2",
    )

    @classmethod
    def similarity(

        cls,

        skill1: str,

        skill2: str,

    ):

        embedding1 = cls.model.encode(

            skill1,
        )

        embedding2 = cls.model.encode(

            skill2,
        )

        return float(

            cosine_similarity(

                embedding1,

                embedding2,
            )
        )

    @classmethod
    def match(

        cls,

        resume_skills: list[str],

        job_skills: list[str],

        threshold: float = 0.82,

    ):

        matched = []

        missing = []

        semantic_matches = []

        for job_skill in job_skills:

            best_score = 0

            best_resume_skill = None

            for resume_skill in resume_skills:

                score = cls.similarity(

                    resume_skill,

                    job_skill,
                )

                if score > best_score:

                    best_score = score

                    best_resume_skill = resume_skill

            if best_score >= threshold:

                matched.append(

                    job_skill,
                )

                semantic_matches.append(

                    {

                        "resume_skill": best_resume_skill,

                        "job_skill": job_skill,

                        "score": round(

                            best_score,

                            3,
                        ),
                    }
                )

            else:

                missing.append(

                    job_skill,
                )

        return {

            "matched": matched,

            "missing": missing,

            "semantic_matches": semantic_matches,
        }