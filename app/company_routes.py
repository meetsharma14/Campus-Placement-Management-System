<<<<<<< HEAD
from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models.company import Company
from app.utils.jwt_handler import create_token
from passlib.hash import bcrypt
from app.models.job import Job
from app.utils.auth import get_current_user, require_role
router = APIRouter()

# Company Register
@router.post("/companies/register")
def register(company: dict):
    db = SessionLocal()

    new_company = Company(
        company_name=company["company_name"],
        hr_email=company["hr_email"],
        password=bcrypt.hash(company["password"])
    )

    db.add(new_company)
    db.commit()
    db.close()

    return {"message": "Company registered successfully"}


# Company Login
@router.post("/companies/login")
def login(data: dict):
    db = SessionLocal()

    company = db.query(Company).filter(
        Company.hr_email == data["hr_email"]
    ).first()

    if not company:
        return {"error": "Company not found"}

    if not bcrypt.verify(data["password"], company.password):
        return {"error": "Invalid password"}

    if not company.approved:
        return {"error": "Company not approved by admin"}

    return {
        "token": create_token({
            "id": company.id,
            "role": "company"
        })
    }
# Create Job
# Create Job
@router.post("/jobs")
def create_job(
    job: dict,
    user=Depends(require_role("company"))
):
    db = SessionLocal()

    new_job = Job(
        company_id=user["id"],   # fixed here
        title=job["title"],
        description=job["description"],
        min_cgpa=job["min_cgpa"],
        branch=job["branch"],
        salary=job["salary"]
    )

    db.add(new_job)
    db.commit()
    db.close()

    return {"message": "Job created successfully"}


# Get All Jobs
@router.get("/jobs")
def get_jobs():
    db = SessionLocal()

    jobs = db.query(Job).all()

    return jobs
=======
from fastapi import APIRouter
from app.database import SessionLocal
from app.models.company import Company
from app.utils.jwt_handler import create_token
from passlib.hash import bcrypt
from app.models.job import Job
from app.utils.auth import get_current_user, require_role

router = APIRouter()

# Company Register
@router.post("/companies/register")
def register(company: dict):
    db = SessionLocal()

    new_company = Company(
        company_name=company["company_name"],
        hr_email=company["hr_email"],
        password=bcrypt.hash(company["password"])
    )

    db.add(new_company)
    db.commit()
    db.close()

    return {"message": "Company registered successfully"}


# Company Login
@router.post("/companies/login")
def login(data: dict):
    db = SessionLocal()

    company = db.query(Company).filter(
        Company.hr_email == data["hr_email"]
    ).first()

    if not company:
        return {"error": "Company not found"}

    if not bcrypt.verify(data["password"], company.password):
        return {"error": "Invalid password"}

    if not company.approved:
        return {"error": "Company not approved by admin"}

    return {
        "token": create_token({
            "id": company.id,
            "role": "company"
        })
    }
# Create Job
@router.post("/jobs")
def create_job(job: dict,
    user=Depends(require_role("company"))):
    db = SessionLocal()

    new_job = Job(
        company_id=job["company_id"],
        title=job["title"],
        description=job["description"],
        min_cgpa=job["min_cgpa"],
        branch=job["branch"],
        salary=job["salary"]
    )

    db.add(new_job)
    db.commit()
    db.close()

    return {"message": "Job created successfully"}


# Get All Jobs
@router.get("/jobs")
def get_jobs():
    db = SessionLocal()

    jobs = db.query(Job).all()

    return jobs
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
