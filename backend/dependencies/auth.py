from jose import jwt, JWTError
from datetime import datetime , timedelta
from dotenv import load_dotenv
import os
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer,HTTPBearer, HTTPAuthorizationCredentials
# from backend.core.security import SECRET_KEY, ALGORITHM

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


def create_access_token(data:dict):
    data["exp"] = datetime.utcnow() + timedelta(minutes=20)
    return jwt.encode(data, SECRET_KEY ,algorithm=ALGORITHM)

# user authotetication user token is right or not 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



security = HTTPBearer()
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

def admin_only(user: dict = Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    return user