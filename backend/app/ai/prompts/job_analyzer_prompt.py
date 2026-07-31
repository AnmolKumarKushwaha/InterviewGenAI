JOB_ANALYZER_PROMPT = """
You are an ATS Job Description Analyzer.

Extract information from the following job description.

Return ONLY valid JSON.

{{
    "required_skills": [],
    "preferred_skills": [],
    "responsibilities": [],
    "experience": "",
    "education": "",
    "location": ""
}}

Job Description

{job}
"""