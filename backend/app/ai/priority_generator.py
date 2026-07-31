from app.ai.skill_weights import SKILL_WEIGHTS


class PriorityGenerator:

    @staticmethod
    def generate(
        missing_skills,
    ):

        priorities = []

        for skill in missing_skills:

            weight = SKILL_WEIGHTS.get(
                skill.lower(),
                1,
            )

            if weight >= 5:

                priority = "High"

            elif weight >= 3:

                priority = "Medium"

            else:

                priority = "Low"

            priorities.append(

                {

                    "skill": skill,

                    "priority": priority,

                }

            )

        return priorities