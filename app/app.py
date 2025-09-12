from fastapi import FastAPI
from app.auth import routes as auth_routes
from app.core.database import Base, engine

# Create database tables (good for dev; for prod, use Alembic migrations)
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Personal Finance Tracker")

# Include routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])

# Root endpoint (sanity check)
@app.get("/")
def read_root():
    return {"message": "Personal Finance Tracker API is running"}
