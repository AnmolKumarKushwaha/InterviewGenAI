EXPLANATION_PROMPT = """
You are an expert technical interviewer.

For every missing skill, return:

1. Skill
2. Why it is important
3. Learning priority
4. Estimated learning time
5. Best free learning resource

Return ONLY valid JSON.

Example:

[
    {{
        "skill":"Docker",
        "importance":"Docker simplifies deployment.",
        "priority":"High",
        "learning_time":"2 weeks",
        "resource":"https://docs.docker.com"
    }}
]

Missing Skills:

{skills}
"""