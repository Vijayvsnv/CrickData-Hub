from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from backend.schemas import RegisterSchema,LoginSchema
from backend.db import SessionLocal
from backend.models import User
from backend.core.security import hash_pass,verify_password
from backend.dependencies.auth import create_access_token



router =  APIRouter(prefix="/auth", tags=["Auth"])
def get_db():
    db = SessionLocal()
    try :
        yield db

    finally :
        db.close()



@router.post("/register")
def register(
    user: RegisterSchema,
    db: Session = Depends(get_db)
):
    hashed = hash_pass(user.password)
    new_user = User(
        username=user.username,
        password=hashed,
        role=user.role
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered successfully"}


@router.post("/login")
def login(
    user: LoginSchema,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "user_id": db_user.id,
        "role": db_user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": db_user.role
    }