<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./placement.db"

engine = create_engine(
DATABASE_URL,
connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
autocommit=False,
autoflush=False,
bind=engine
)

Base = declarative_base()
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./placement.db"

engine = create_engine(
DATABASE_URL,
connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
autocommit=False,
autoflush=False,
bind=engine
)

Base = declarative_base()
>>>>>>> 9ae8fc84428353b2bcc0126879f357f56f165a61
