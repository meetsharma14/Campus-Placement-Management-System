from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models.company import Company
from app.models.student import Student
from app.models.job import Job
from app.models.application import Application
from app.utils.auth import get_current_user, require_role


router = APIRouter()


@router.get("/admin/students")
def get_students (user=Depends(require_role("admin"))):
    db = SessionLocal()
    students = db.query(Student).all()
    return students


@router.get("/admin/companies")
def get_companies(user=Depends(require_role("admin"))):
    db = SessionLocal()
    companies = db.query(Company).all()
    return db.query(companies).all()


@router.put("/admin/companies/{company_id}/approve")
def approve_company(company_id: str,user=Depends(require_role("admin"))):
    db = SessionLocal()

    company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not company:
        return {"error": "Company not found"}

    company.approved = True
    db.commit()

    return {"message": "Company approved successfully"}
@router.get("/admin/analytics")
def analytics(user=Depends(require_role("admin"))):
    db = SessionLocal()

    total_students = db.query(Student).count()
    total_companies = db.query(Company).count()
    total_jobs = db.query(Job).count()
    total_applications = db.query(Application).count()

    return {
        "total_students": total_students,
        "total_companies": total_companies,
        "total_jobs": total_jobs,
        "total_applications": total_applications
    }
@router.put("/admin/applications/{application_id}")
def update_application_status(application_id: int, status: str,user=Depends(require_role("admin"))):
    db = SessionLocal()

    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    if not application:
        return {"error": "Application not found"}

    application.status = status
    db.commit()
    db.close()

    return {
        "message": "Application status updated",
        "new_status": status
    }

