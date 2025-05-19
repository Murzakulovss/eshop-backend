def test_create_user(client):
    response = client.post("/users/", json = {"email": "user@example.com","password": "string"})
    data = response.json()
    assert response.status_code == 200
    assert data["email"] == "user@example.com"
    assert isinstance(data["id"], int)
    assert data["is_active"] is True

def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    user = data[0]
    assert "email" in user
    assert "id" in user
    assert "is_active" in user
    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)
    assert isinstance(user["is_active"], bool)

def test_read_user_by_id(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "string"})
    user_id = response.json()["id"]
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["email"] == "user@example.com"
    assert get_response.json()["id"] == user_id
    assert get_response.json()["is_active"] is True

def test_update_user(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "string"})
    user_id = response.json()["id"]
    put_response = client.put(f"/users/{user_id}", json={"email": "change_mail@example.com"})
    assert put_response.status_code == 200
    assert put_response.json()["email"] == "change_mail@example.com"

def test_delete_user(client):
    response = client.post("/users/", json={"email": "user@example.com", "password": "string"})
    user_id = response.json()["id"]
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200


