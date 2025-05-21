from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email==email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db:Session,skip: int = 0, limit = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(email = user.email, hashed_password = hash_password(user.password), is_active = True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db:Session, user_email: str, user_id:int):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    user.email = user_email
    db.commit()
    db.refresh(user)
    return user

def delete_user(db:Session, user_id:int):
    user = get_user_by_id(db,user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user







