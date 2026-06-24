from fastapi import Header
from app.utils.jwt_handler import verify_token


def get_current_user(token: str = Header(...)):
    payload = verify_token(token)

    if not payload:
        return {"error": "Invalid token"}

    return payload
