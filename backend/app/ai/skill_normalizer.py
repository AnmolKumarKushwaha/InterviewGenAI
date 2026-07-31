import json
from pathlib import Path


class SkillNormalizer:

    _synonyms = None

    @classmethod
    def load(cls):

        if cls._synonyms is not None:

            return cls._synonyms

        path = (
            Path(__file__)
            .parent.parent
            / "data"
            / "skill_synonyms.json"
        )

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:

            raw = json.load(file)

        mapping = {}

        for canonical, aliases in raw.items():

            mapping[canonical.lower()] = canonical.lower()

            for alias in aliases:

                mapping[
                    alias.lower()
                ] = canonical.lower()

        cls._synonyms = mapping

        return mapping

    @classmethod
    def normalize_skill(

        cls,

        skill: str,

    ):

        mapping = cls.load()

        skill = skill.lower().strip()

        return mapping.get(
            skill,
            skill,
        )

    @classmethod
    def normalize_list(

        cls,

        skills: list[str],

    ):

        normalized = []

        seen = set()

        for skill in skills:

            skill = cls.normalize_skill(
                skill,
            )

            if skill not in seen:

                normalized.append(
                    skill,
                )

                seen.add(
                    skill,
                )

        return normalized