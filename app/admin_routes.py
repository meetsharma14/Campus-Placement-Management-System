from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models.company import Company
from app.models.student import Student
from app.models.job import Job
from app.models.application import Application
from app.utils.auth import require_role
from app.utils.jwt_handler import create_token

router = APIRouter()


@router.post("/admin/login")
def admin_login(data: dict):
    if data["email"] == "admin@gmail.com" and data["password"] == "admin123":
        token = create_token({
            "id": 0,
            "role": "admin"
        })
        return {"token": token}

    return {"error": "Invalid admin credentials"}


@router.get("/admin/students")
def get_students(user=Depends(require_role("admin"))):
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students


@router.get("/admin/companies")
def get_companies(user=Depends(require_role("admin"))):
    db = SessionLocal()
    companies = db.query(Company).all()
    db.close()
    return companies


@router.put("/admin/companies/{company_id}/approve")
def approve_company(company_id: str, user=Depends(require_role("admin"))):
    db = SessionLocal()

    company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not company:
        db.close()
        return {"error": "Company not found"}

    company.approved = True
    db.commit()
    db.close()

    return {"message": "Company approved successfully"}

# delete company
@router.delete("/admin/companies/{company_id}")
def delete_company(
    company_id: str,
    user=Depends(require_role("admin"))
):
    db = SessionLocal()

    company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not company:
        db.close()
        return {"error": "Company not found"}

    db.delete(company)
    db.commit()
    db.close()

    return {
        "message": "Company deleted successfully"
    }


@router.get("/admin/analytics")
def analytics(user=Depends(require_role("admin"))):
    db = SessionLocal()

    data = {
        "total_students": db.query(Student).count(),
        "total_companies": db.query(Company).count(),
        "total_jobs": db.query(Job).count(),
        "total_applications": db.query(Application).count()
    }

    db.close()
    return data


@router.put("/admin/applications/{application_id}")
def update_application_status(
    application_id: int,
    status: str,
    user=Depends(require_role("admin"))
):
    db = SessionLocal()

    application = db.query(Application).filter(
        Application.id == application_id
    ).first()

    if not application:
        db.close()
        return {"error": "Application not found"}

    application.status = status
    db.commit()
    db.close()

    return {
        "message": "Application status updated",
        "new_status": status
    }
@router.delete("/admin/jobs/{job_id}")
def delete_job(
    job_id: str,
    user=Depends(require_role("admin"))
):
    db = SessionLocal()

    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        db.close()
        return {"error": "Job not found"}

    db.delete(job)
    db.commit()
    db.close()

    return {"message": "Job deleted successfully"}
@router.get("/admin/applications")
def get_all_applications(
    user=Depends(require_role("admin"))
):
    db = SessionLocal()

    applications = (
        db.query(Application, Student, Job, Company)
        .join(Student, Application.student_id == Student.id)
        .join(Job, Application.job_id == Job.id)
        .join(Company, Job.company_id == Company.id)
        .all()
    )

    result = []

    for app, student, job, company in applications:
        result.append({
            "id": app.id,
            "student_name": student.name,
            "company_name": company.company_name,
            "job_title": job.title,
            "status": app.status
        })

    db.close()
    return result
