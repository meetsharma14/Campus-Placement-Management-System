from jose import jwt

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def create_token(data: dict):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except:
        return None
