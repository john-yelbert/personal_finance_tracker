from sqlalchemy.orm import Session
from app.users import models, schema
from app.core.security import hash_password
from datetime import timedelta

def register_user(db: Session, user: schema.UserCreate):
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


