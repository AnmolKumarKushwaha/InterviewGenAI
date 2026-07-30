class ATSScore:

    @staticmethod
    def calculate(
        analysis: dict,
        text: str,
    ):

        score = 0

        breakdown = {}

        # -------------------------
        # Skills
        # -------------------------

        skills = analysis.get(
            "skills",
            [],
        )

        skills_score = min(
            len(skills) * 2,
            20,
        )

        score += skills_score

        breakdown["skills"] = skills_score

        # -------------------------
        # Projects
        # -------------------------

        projects = analysis.get(
            "projects",
            [],
        )

        project_score = min(
            len(projects) * 5,
            20,
        )

        score += project_score

        breakdown["projects"] = project_score

        # -------------------------
        # Experience
        # -------------------------

        experience = analysis.get(
            "experience",
            [],
        )

        experience_score = 20 if experience else 0

        score += experience_score

        breakdown["experience"] = experience_score

        # -------------------------
        # Education
        # -------------------------

        education = analysis.get(
            "education",
            [],
        )

        education_score = 10 if education else 0

        score += education_score

        breakdown["education"] = education_score

        # -------------------------
        # Certifications
        # -------------------------

        certifications = analysis.get(
            "certifications",
            [],
        )

        certification_score = min(
            len(certifications) * 2,
            10,
        )

        score += certification_score

        breakdown["certifications"] = certification_score

        # -------------------------
        # Resume Length
        # -------------------------

        words = len(
            text.split(),
        )

        if 350 <= words <= 900:

            length_score = 10

        elif words >= 200:

            length_score = 5

        else:

            length_score = 0

        score += length_score

        breakdown["length"] = length_score

        # -------------------------
        # Contact Information
        # -------------------------

        contact_score = 0

        if "@" in text:

            contact_score += 5

        if "+" in text:

            contact_score += 5

        score += contact_score

        breakdown["contact"] = contact_score

        return {

            "score": min(
                score,
                100,
            ),

            "breakdown": breakdown,
        }