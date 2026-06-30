from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt_handler import verify_token

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    print("Received token:", token)

    payload = verify_token(token)
    print("Decoded payload:", payload)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        print("Current user:", user)

        if user["role"] != role:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return user

    return role_checker
    return wrapper
