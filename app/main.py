from fastapi import FastAPI
from app.api import users
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users.router, prefix="/users", tags=["users"])
