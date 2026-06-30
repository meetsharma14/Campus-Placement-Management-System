from fastapi import APIRouter, UploadFile, File
from app.database import SessionLocal
from app.models.student import Student
from app.models.application import Application
import shutil
import os
from fastapi import Depends
from app.utils.auth import get_current_user, require_role
from app.utils.jwt_handler import create_token
from app.models.job import Job
from app.models.company import Company
from app.auth import hash_password

router = APIRouter()

@router.post("/students/register")
def register(student: dict):
    db = SessionLocal()

    existing_student = db.query(Student).filter(
        Student.email == student["email"]
    ).first()

    if existing_student:
        db.close()
        return {"error": "Email already exists"}

    # ✅ STEP 1: get password safely
    password = str(student.get("password", ""))

    # ✅ STEP 2: debug (IMPORTANT)
    print("RAW PASSWORD:", password)
    print("LENGTH:", len(password.encode("utf-8")))

    # ✅ STEP 3: FIX (truncate before bcrypt)
    if len(password.encode("utf-8")) > 72:
        password = password[:72]

    # ✅ STEP 4: hash AFTER fix
    from passlib.hash import argon2

    hashed_password = argon2.hash(student["password"])

    new_student = Student(
        name=student["name"],
        email=student["email"],
        password=hashed_password
    )

    db.add(new_student)
    db.commit()
    db.close()

    return {"message": "Student registered successfully"}


@router.post("/students/login")
def login(data: dict):
    db = SessionLocal()

    student = db.query(Student).filter(
        Student.email == data["email"]
    ).first()

    if not student or not bcrypt.verify(
        data["password"],
        student.password
    ):
        db.close()
        return {"error": "Invalid credentials"}

    token = create_token({
        "id": student.id,
        "role": "student"
    })

    db.close()

    return {
        "token": token
    }

@router.put("/students/profile")
def update_profile(
    data: dict,
    user=Depends(require_role("student"))
):
    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == user["id"]
    ).first()

    if not student:
        db.close()
        return {"error": "Student not found"}

    student.cgpa = data["cgpa"]
    student.branch = data["branch"]
    student.graduation_year = data["graduation_year"]

    db.commit()
    db.close()

    return {"message": "Profile updated successfully"}

@router.post("/resume/upload")
def upload_resume(file: UploadFile,
    user=Depends(get_current_user)):
    os.makedirs("uploads", exist_ok=True)


    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"resume_url": path}

@router.get("/test")
def test():
    return {"message": "Student routes working"}

@router.post("/jobs/{job_id}/apply")
def apply_job(
    job_id: str,
    user=Depends(require_role("student"))
):
    db = SessionLocal()

    existing_application = db.query(Application).filter(
        Application.student_id == user["id"],
        Application.job_id == job_id
    ).first()

    if existing_application:
        db.close()
        return {"error": "Already applied"}

    new_application = Application(
        student_id=user["id"],
        job_id=job_id,
        status="Applied"
    )

    db.add(new_application)
    db.commit()
    db.close()

    return {"message": "Applied successfully"}
@router.get("/students/{student_id}/applications")
def get_my_applications(student_id: str):
    db = SessionLocal()

    applications = (
        db.query(Application, Job, Company)
        .join(Job, Application.job_id == Job.id)
        .join(Company, Job.company_id == Company.id)
        .filter(Application.student_id == student_id)
        .all()
    )

    result = []

    for app, job, company in applications:
        result.append({
            "application_id": app.id,
            "company_name": company.company_name,
            "job_title": job.title,
            "status": app.status
        })

    db.close()
    return result
@router.get("/students/{student_id}")
def get_student(student_id: str):
    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        db.close()
        return {"error": "Student not found"}
    db.close()
    return student
