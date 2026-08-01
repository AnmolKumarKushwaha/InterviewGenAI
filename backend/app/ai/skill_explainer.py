SKILL_INFORMATION = {

    "spring boot": {

        "importance": "Used to build scalable Java backend applications.",

        "difficulty": "Intermediate",

        "learning_time": "2-3 weeks",

    },

    "docker": {

        "importance": "Required for containerizing applications.",

        "difficulty": "Beginner",

        "learning_time": "1 week",

    },

    "aws": {

        "importance": "Widely used cloud platform for deployment.",

        "difficulty": "Intermediate",

        "learning_time": "2 weeks",

    },

    "postgresql": {

        "importance": "Popular relational database for backend systems.",

        "difficulty": "Beginner",

        "learning_time": "1 week",

    },

    "redis": {

        "importance": "Used for caching and improving performance.",

        "difficulty": "Intermediate",

        "learning_time": "4-5 days",

    },

}


class SkillExplainer:

    @staticmethod
    def generate(
        missing_skills,
    ):

        explanations = []

        for skill in missing_skills:

            info = SKILL_INFORMATION.get(

                skill.lower(),

                {

                    "importance": "Important skill for this role.",

                    "difficulty": "Unknown",

                    "learning_time": "Unknown",

                },

            )

            explanations.append(

                {

                    "skill": skill,

                    "importance": info["importance"],

                    "why_missing": f"{skill} appears in the job description but not in your resume.",

                    "difficulty": info["difficulty"],

                    "learning_time": info["learning_time"],

                }

            )

        return explanations