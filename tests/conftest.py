import pytest
from starlette.testclient import TestClient
from app.main import app
from tests.test_users import create_user


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
