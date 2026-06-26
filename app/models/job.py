<<<<<<< HEAD
from sqlalchemy import Column, String, Float, ForeignKey
from app.database import Base
import uuid

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = Column(String, ForeignKey("companies.id"))
    title = Column(String)
    description = Column(String)
    min_cgpa = Column(Float)
    branch = Column(String)
=======
from sqlalchemy import Column, String, Float, ForeignKey
from app.database import Base
import uuid

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = Column(String, ForeignKey("companies.id"))
    title = Column(String)
    description = Column(String)
    min_cgpa = Column(Float)
    branch = Column(String)
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
    salary = Column(Float)