from app.security.jwt import create_access_token
from app.security.jwt import decode_access_token

token = create_access_token(
    {
        "sub": "admin@gmail.com",
    }
)

print(token)

print(
    decode_access_token(
        token,
    )
)