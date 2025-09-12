from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.users import schema
from app.auth import services

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=schema.UserRead)
def register(user: schema.UserCreate, db: Session = Depends(get_db)):
    return services.register_user(db, user)


