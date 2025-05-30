Eshop is a backend project for an online store. It includes:
User registration and authentication (JWT)
Full CRUD operations for products

-
Tech stack:
-

-Python 3.11
-FastAPI
-SQLAlchemy
-Alembic (migrations)
-PostgresSQL
-Pydantic
-Pytest (tests)
-Docker (optional)

-
Installation:
-

git clone https://github.com/Murzakulovss/eshop-backend.git
cd eshop-backend
poetry install
cp .env.example .env
alembic upgrade head
poetry run uvicorn app.main:app --reload

-
.env example
-

DB_HOST=localhost
DB_PORT=5432
DB_NAME=eshop_db
DB_USER=eshop_user
DB_PASSWORD=supersecret
SECRET_KEY=your_secret_key

-
tests
-

poetry run pytest