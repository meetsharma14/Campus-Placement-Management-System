<<<<<<< HEAD
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
=======
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
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
    resume_url = Column(String)