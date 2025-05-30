from fastapi import FastAPI
from app.api.routers import users, product
from app.api.routers.auth import auth
from fastapi.openapi.utils import get_openapi

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Eshop"}

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(auth.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="eshop API",
        version="1.0.0",
        description="Документация API с авторизацией через JWT",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

