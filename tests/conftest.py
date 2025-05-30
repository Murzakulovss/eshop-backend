import pytest
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from app.db import SessionLocal
from app.main import app
from app.domain.models import Product, User
from tests.test_users import create_user

@pytest.fixture(autouse=True)
def clean_db():
    db: Session = SessionLocal()
    db.query(Product).delete()
    db.query(User).delete()
    db.commit()
    db.close()

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture()
def test_user(client):
    return create_user(client)

@pytest.fixture
def auth_header(test_user, client):
    response = client.post("/login", data={"username": test_user["email"], "password": "string"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

