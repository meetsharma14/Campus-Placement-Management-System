from fastapi import APIRouter, UploadFile, File
from app.database import SessionLocal
from app.models.student import Student
from app.models.application import Application
from passlib.hash import bcrypt
import shutil
import os
from app.models.application import Application
from fastapi import Depends
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/students/register")
def register(student: dict):
    db = SessionLocal()


    new_student = Student(
        name=student["name"],
        email=student["email"],
        password=bcrypt.hash(student["password"]),
        cgpa=student["cgpa"],
        branch=student["branch"],
        graduation_year=student["graduation_year"]
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
        return {"error": "Invalid credentials"}

    return {
        "token": create_token({
            "id": student.id,
            "role": "student"
        })
    }


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
    student_id: user["id"],
    user=Depends(require_role("student"))
):
    db = SessionLocal()


    new_application = Application(
        student_id=student_id,
        job_id=job_id,
        status="Applied"
    )

    db.add(new_application)
    db.commit()
    db.close()

    return {"message": "Applied successfully"}
@router.get("/students/{student_id}/applications")
def get_my_applications(student_id: int):
    db = SessionLocal()

    applications = db.query(Application).filter(
        Application.student_id == student_id
    ).all()

    return applications
@router.get("/students/{student_id}")
def get_student(student_id: int):
    db = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return {"error": "Student not found"}

    return student


