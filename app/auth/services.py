from sqlalchemy.orm import Session
from app.users import models, schema
from app.core.security import hash_password
from datetime import timedelta
from fastapi import HTTPException, status


def register_user(db: Session, user: schema.UserCreate):
    existing_user = db.query(models.User).filter(
        (models.User.email == user.email) | 
        (models.User.username == user.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )
    
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        profession=user.profession,
        income=user.income
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


