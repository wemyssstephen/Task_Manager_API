import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# TODO: update to use environment variables
POSTGRESQL_PASSWORD = os.environ['POSTGRESQL_PASSWORD']
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{POSTGRESQL_PASSWORD}@localhost/task_management"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()