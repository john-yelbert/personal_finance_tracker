from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL - pulled from environment variables (Docker Compose will provide this)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://finance_tracker_user:finance_tracker_pass@localhost:5432/finance_tracker_db"
)

# Create the engine - creates a connection to PostgreSQL db in docker
engine = create_engine(DATABASE_URL, echo=True, future=True)


# Base class for all models to inherit from
Base = declarative_base()


# Dependency for FastAPI routes (ensures session is opened and closed correctly)
def get_db():
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try:
        yield db_session
    finally:
        db_session.close()
