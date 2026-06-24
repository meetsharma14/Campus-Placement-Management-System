from fastapi import FastAPI
from app import student_routes, company_routes, admin_routes
from app.database import Base, engine

# Import all models
from app.models.student import Student
from app.models.company import Company
from app.models.job import Job
from app.models.application import Application

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Campus Placement Management System",
    description="API for Students, Companies, and Placement Officers",
    version="1.0.0"
)

app.include_router(student_routes.router)
app.include_router(company_routes.router)
app.include_router(admin_routes.router)

@app.get("/")
def home():
    return {
        "message": "Campus Placement System API is running"
    }
