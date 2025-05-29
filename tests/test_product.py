from http.client import responses
from app.models import Product

def create_product_test(client, auth_header, name, description, price):
    return client.post("/products/", headers = auth_header, json={
        "name": name,
        "description": description,
        "price": price
    })

def test_create_product(client, auth_header):
    response = client.post("/products/", headers=auth_header, json={
        "name": "-",
        "description": "-",
        "price": 999
    })
    assert response.status_code == 200
    assert response.json()["name"] == "-"

def test_read_product_by_id(client, auth_header):
    response = create_product_test(client, auth_header, name="test read", description="read desc", price=100)
    assert response.status_code == 200
    product = response.json()
    product_id = product["id"]

    response = client.get(f"/products/{product_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test read"
    assert data["id"] == product_id

def test_read_products(client, auth_header):
    response = client.get("/products/", headers=auth_header)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_product(client, auth_header):
    response = create_product_test(client, auth_header, name="old name", description="old desc", price=100)
    product_id = response.json()["id"]

    update_response = client.put(f"/products/{product_id}", headers=auth_header, json={
        "name": "New Name",
        "description": "Updated Description",
        "price": 700
    })

    assert update_response.status_code == 200
    updated = update_response.json()
    assert updated["name"] == "New Name"
    assert updated["price"] == 700

def test_delete_product(client, auth_header):
    response = create_product_test(client, auth_header, name="delete", description="temporary", price=100)
    product_id = response.json()["id"]

    delete_response = client.delete(f"/products/{product_id}", headers=auth_header)
    assert delete_response.status_code == 200

    get_response = client.get(f"/products/{product_id}", headers=auth_header)
    assert get_response.status_code == 404



