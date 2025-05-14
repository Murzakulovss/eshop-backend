from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(min_length=3)

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserInDB(UserRead):
    hashed_password: str
