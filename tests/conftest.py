from dotenv import load_dotenv
import pytest, os
load_dotenv()
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..app import models
from ..app.database import  get_db, Base
from ..app.main import app

POSTGRESQL_PASSWORD = os.environ['POSTGRESQL_PASSWORD']
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{POSTGRESQL_PASSWORD}@localhost/task_management_test"

@pytest.fixture(scope='session')
def test_engine():
    # Creates test engine
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # Create all tables
    Base.metadata.create_all(bind=engine)
    yield engine
    # Drops all tables after tests are done
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(test_engine):
    # Creates a new session for each test
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def client(db_session):
    # Override the get_db dependency to use test database
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db

    # Create test client
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture(autouse=True)
def clear_db(db_session):
    yield
    db_session.query(models.TaskModel).delete()
    db_session.commit()

