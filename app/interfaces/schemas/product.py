from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int

class ProductCreate(ProductBase):
    pass

class ProductRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: int
    owner_id: int

    model_config = {
        "from_attributes": True
    }

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt = 0)



