from fastapi import Header, HTTPException
from app.utils.jwt_handler import verify_token


def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token missing"
        )

    token = authorization.split(" ")[1]
    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


def require_role(role: str):
    def role_checker(user=Header(None)):
        return get_current_user
    return role_checker
