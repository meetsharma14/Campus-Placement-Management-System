from fastapi import APIRouter
from app.database import SessionLocal
from app.models.company import Company
from app.models.student import Student
from app.models.job import Job
from app.models.application import Application

router = APIRouter()


@router.get("/admin/students")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    return students


@router.get("/admin/companies")
def get_companies():
    db = SessionLocal()
    companies = db.query(Company).all()
    return companies


@router.put("/admin/companies/{company_id}/approve")
def approve_company(company_id: str):
    db = SessionLocal()

    company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not company:
        return {"error": "Company not found"}

    company.approved = True
    db.commit()

    return {"message": "Company approved successfully"}