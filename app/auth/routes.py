from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.users import schemas
from app.auth import services

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=schemas.UserRead)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.register_user(db, user)

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = services.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = services.create_user_token(user)
    return {"access_token": token, "token_type": "bearer"}
