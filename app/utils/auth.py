<<<<<<< HEAD
from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt_handler import verify_token

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload


def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )
        return user
    return role_checker
=======
from fastapi import Header
from app.utils.jwt_handler import verify_token


def get_current_user(token: str = Header(...)):
    payload = verify_token(token)

    if not payload:
        return {"error": "Invalid token"}

    return payload
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
