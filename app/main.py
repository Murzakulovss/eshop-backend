from fastapi import FastAPI
from app.api.routers import users
from app.api.routers import auth

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router)
