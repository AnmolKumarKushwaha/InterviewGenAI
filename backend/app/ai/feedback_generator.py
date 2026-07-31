class FeedbackGenerator:

    @staticmethod
    def generate(
        matched,
        missing,
        percentage,
    ):

        if percentage >= 90:

            return (
                "Excellent match. Your resume already covers almost every required skill. "
                "Focus on interview practice and advanced projects."
            )

        if percentage >= 75:

            return (
                f"You already possess {len(matched)} important skills. "
                f"Learning {', '.join(missing)} will make your profile much stronger."
            )

        if percentage >= 50:

            return (
                "Your profile has a solid foundation, but several important skills are still missing. "
                f"Prioritize learning {', '.join(missing[:3])}."
            )

        return (
            "Your profile currently has a significant skill gap. "
            "Start with the core missing technologies before attempting interviews."
        )