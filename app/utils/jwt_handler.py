<<<<<<< HEAD
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
=======
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
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
