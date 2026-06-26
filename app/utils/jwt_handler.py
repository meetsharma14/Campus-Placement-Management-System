from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"


def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload
    except:
        return None
