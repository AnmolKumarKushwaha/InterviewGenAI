CAREER_REPORT_PROMPT = """
You are an experienced Software Engineering Career Coach.

Analyze the candidate profile below.

Resume Skills:
{resume_skills}

Missing Skills:
{missing_skills}

Match Percentage:
{match_percentage}

Learning Priorities:
{learning_priorities}

Skill Explanations:
{skill_explanations}

Learning Roadmap:
{learning_roadmap}

Interview Preparation:
{interview_preparation}

Generate a complete career report.

Return ONLY valid JSON.

Example:

{{
    "ats_score": 82,

    "resume_strengths":[
        "Strong Java knowledge",
        "Good DSA background"
    ],

    "resume_weaknesses":[
        "Missing Spring Boot"
    ],

    "career_summary":"...",    

    "next_steps":[
        "...",
        "...",
        "..."
    ],

    "final_advice":"..."
}}
"""