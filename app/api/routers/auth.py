from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token, SECRET_KEY
from sqlalchemy.orm import Session
from app.crud.user import User, get_user_by_email
from app.db.session import get_db
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer("login")
execution_401 = HTTPException(status_code=401, detail="Invalid email or password")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db = db, email=form_data.username)
    if not user:
        raise execution_401

    password = verify_password(plain_password=form_data.password, hashed_password=user.hashed_password)
    if not password:
        raise execution_401

    access_token = create_access_token(data = {"sub":user.email})
    return {"access_token": access_token,"token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    payload = jwt.decode(token=token, key= SECRET_KEY, algorithms= "HS256")
    email = payload["sub"]
    if not email:
        raise execution_401
    user = get_user_by_email(db=db, email=email)
    if not user:
        raise execution_401
    return user