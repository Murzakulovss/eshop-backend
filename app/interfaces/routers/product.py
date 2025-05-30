from typing import List
from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.interfaces.routers.auth.auth import get_current_user
from app.db.session import get_db

from app.crud.product import (
    get_product_by_id,
    create_product as create_product_crud,
    get_products as get_products_crud,
    update_product as update_product_crud,
    delete_product as delete_product_crud
)
from app.domain.models import User
from app.interfaces.schemas.product import ProductRead, ProductCreate, ProductUpdate

router = APIRouter()

@router.post("/",response_model=ProductRead)
async def create_product(product: ProductCreate, db: Session= Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_product_crud(db=db, product=product, owner_id=current_user.id)

@router.get("/{product_id}", response_model= ProductRead)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db=db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=List[ProductRead])
async def get_products(limit: int = 100,skip:int=0, db: Session = Depends(get_db)):
    return get_products_crud(db=db, limit=limit, skip=skip)

@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_update: ProductUpdate, product_id:int, db:Session = Depends(get_db)):
    updated_product = update_product_crud(db=db,product_id=product_id,name=product_update.name, description=product_update.description, price=product_update.price)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Updating product not found")
    return updated_product

@router.delete("/{product_id}", response_model=ProductRead)
async def delete_product(product_id: int, db: Session=Depends(get_db)):
    deleted_product = delete_product_crud(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Deleting product not found")
    return deleted_product


