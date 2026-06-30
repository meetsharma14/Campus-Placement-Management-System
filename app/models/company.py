from sqlalchemy import Column, String, Boolean
from app.database import Base
import uuid

class Company(Base):
    __tablename__ = "companies"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_name = Column(String)
    hr_email = Column(String, unique=True)
    password = Column(String)
    approved = Column(Boolean, default=False)
