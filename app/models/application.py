from sqlalchemy import Column, String, Float, ForeignKey, Integer
from app.database import Base
import uuid

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"))
    job_id = Column(String, ForeignKey("jobs.id"))
    status = Column(String, default="Applied")