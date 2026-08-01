INTERVIEW_PROMPT = """
You are a Senior Software Engineer and Technical Interviewer.

Using the candidate information below, generate a personalized interview preparation guide.

Resume Skills:
{resume_skills}

Missing Skills:
{missing_skills}

Learning Priorities:
{learning_priorities}

Skill Explanations:
{skill_explanations}

Learning Roadmap:
{learning_roadmap}

Return ONLY valid JSON.

Example:

[
    {{
        "technical_questions":[
            {{
                "question":"Explain Dependency Injection.",
                "expected_answer":"..."
            }}
        ],

        "hr_questions":[
            {{
                "question":"Tell me about yourself.",
                "tip":"Focus on projects."
            }}
        ],

        "coding_topics":[
            "Spring Boot",
            "REST API",
            "PostgreSQL"
        ],

        "interview_tips":[
            "Revise OOP.",
            "Practice SQL joins."
        ]
    }}
]
"""