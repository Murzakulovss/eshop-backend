from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email==email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db:Session, limit = 100):
    return db.query(User).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(email = user.email, hashed_password = hash_password(user.password), is_active = True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user








