from sqlalchemy import Column, String, Float, Integer
from app.database import Base
import uuid

class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    cgpa = Column(Float)
    branch = Column(String)
    graduation_year = Column(Integer)
    resume_url = Column(String)