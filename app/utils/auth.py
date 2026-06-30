from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt_handler import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


def require_role(role: str):
    def wrapper(user=Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return user

    return wrapper
