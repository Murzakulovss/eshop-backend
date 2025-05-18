from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(min_length=3)

class UserRead(UserBase):
    id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

class UserInDB(UserRead):
    hashed_password: str

