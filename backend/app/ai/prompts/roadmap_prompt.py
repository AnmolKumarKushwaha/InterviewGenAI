ROADMAP_PROMPT = """
You are an experienced Software Engineering Mentor.

Your task is to generate a personalized learning roadmap.

The roadmap must be based on:

1. Candidate's existing skills
2. Missing skills
3. Learning priorities
4. Skill explanations

Requirements:

- Generate a practical roadmap.
- Order topics from fundamentals to advanced.
- High-priority skills should appear earlier.
- Every week should contain:
    - Week number
    - Title
    - Topics
    - Goal

Return ONLY valid JSON.

Format:

{{
    "duration":"6 Weeks",

    "summary":"Short career guidance.",

    "roadmap":[

        {{
            "week":1,

            "title":"Backend Basics",

            "topics":[
                "Spring Boot",
                "REST API"
            ],

            "goal":"Build your first backend API."
        }}

    ]
}}

Resume Skills

{resume_skills}

Missing Skills

{missing_skills}

Learning Priorities

{learning_priorities}

Skill Explanations

{skill_explanations}
"""