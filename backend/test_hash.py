from app.security.hashing import hash_password
from app.security.hashing import verify_password

password = "InterviewGenAI123"

hashed = hash_password(password)

print(hashed)

print(
    verify_password(
        password,
        hashed,
    )
)