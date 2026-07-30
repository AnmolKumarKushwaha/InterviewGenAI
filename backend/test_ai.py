from app.ai.resume_analyzer import ResumeAnalyzer

text = """
B.Tech Computer Science

Skills:
Java
Python
FastAPI
Docker

Projects:
InterviewGenAI
Spotify Clone
"""

result = ResumeAnalyzer.analyze(text)

print(result)