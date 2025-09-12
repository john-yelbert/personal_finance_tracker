from sqlalchemy.orm import Session
from app.users import models, schemas
from app.core.security import hash_password, verify_password, create_access_token
from datetime import timedelta

def register_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        profession=user.profession,
        income=user.income
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

def create_user_token(user: models.User):
    access_token_expires = timedelta(minutes=30)
    return create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires
    )
