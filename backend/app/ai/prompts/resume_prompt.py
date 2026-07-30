RESUME_ANALYZER_PROMPT = """
You are an expert technical recruiter.

Analyze the resume.

Return ONLY valid JSON.

Schema:

{{
    "skills": [],
    "soft_skills": [],
    "education": [],
    "projects": [],
    "experience": [],
    "certifications": [],
    "resume_score": 0,
    "missing_skills": [],
    "suggestions": []
}}

Resume:

{resume}
"""