from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.crud.user import (
    create_user as create_user_crud,
    get_user_by_id,
    get_users as get_users_crud,
    update_user as update_user_crud,
    delete_user as delete_user_crud,
)
from app.db.session import get_db
from app.interfaces.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()


@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_crud(db=db, user=user)


@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[UserRead])
async def get_users(limit: int = 100, db: Session = Depends(get_db)):
    return get_users_crud(db=db, limit=limit)


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_update: UserUpdate, user_id: int, db: Session = Depends(get_db)):
    updated_user = update_user_crud(db=db, user_id=user_id, user_email=str(user_update.email))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", response_model=UserRead)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user_crud(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
