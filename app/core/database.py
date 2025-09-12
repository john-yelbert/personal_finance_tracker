from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL - pulled from environment variables (Docker Compose will provide this)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://finance_tracker_user:finance_tracker_pass@localhost:5432/finance_tracker_db"
)

# Create the engine (connection to PostgreSQL)
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models to inherit from
Base = declarative_base()


# Dependency for FastAPI routes (ensures session is opened and closed correctly)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
