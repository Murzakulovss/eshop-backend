def create_user(client, email="user@example.com", password="string"):
    return client.post("/users/", json={"email": email, "password": password}).json()

def test_create_user(client):
    data = create_user(client)
    assert data["email"] == "user@example.com"
    assert isinstance(data["id"], int)
    assert data["is_active"] is True

def test_read_users(client):
    create_user(client)
    response = client.get("/users/")
    users = response.json()
    assert response.status_code == 200
    assert isinstance(users, list)
    assert any(user["email"] == "user@example.com" for user in users)

def test_read_user_by_id(client):
    user = create_user(client)
    response = client.get(f"/users/{user['id']}")
    assert response.status_code == 200
    assert response.json()["email"] == user["email"]

def test_update_user(client):
    user = create_user(client)
    updated = client.put(f"/users/{user['id']}", json={"email": "new@example.com"}).json()
    assert updated["email"] == "new@example.com"

def test_delete_user(client):
    user = create_user(client)
    response = client.delete(f"/users/{user['id']}")
    assert response.status_code == 200
