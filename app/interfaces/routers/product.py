from dataclasses import asdict
from typing import List
from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.domain.use_cases.create_product import CreateProductUseCase
from app.domain.use_cases.delete_product import DeleteProductUseCase
from app.domain.use_cases.get_all_products import GetAllProductsUseCase
from app.domain.use_cases.get_product import GetProductUseCase
from app.domain.use_cases.update_product import UpdateProductUseCase
from app.dto.product import ProductUpdateDTO
from app.infrastructure.database.models.user import User
from app.infrastructure.repositoies.product_repository import ProductRepository
from app.interfaces.routers.auth.auth import get_current_user
from app.db.session import get_db
from app.interfaces.schemas.product import ProductRead, ProductCreate, ProductUpdate

router = APIRouter()

@router.post("/", response_model=ProductRead)
async def create_product(product: ProductCreate, db: Session=Depends(get_db), current_user: User = Depends(get_current_user)):
    product_repository = ProductRepository(db)
    use_case = CreateProductUseCase(product_repository)
    result = use_case.execute(
        name=product.name,
        description=product.description,
        price=product.price,
        owner_id=current_user.id)
    return ProductRead(**asdict(result))

@router.get("/{product_id}", response_model=ProductRead)
async def read_product(product_id: int, db: Session=Depends(get_db)):
    product_repository = ProductRepository(db)
    use_case = GetProductUseCase(product_repository)
    result = use_case.execute(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead(**asdict(result))

@router.get("/", response_model= List[ProductRead])
async def read_all_products(db: Session=Depends(get_db)):
    product_repository = ProductRepository(db)
    use_case = GetAllProductsUseCase(product_repository)
    result = use_case.execute()
    return [ProductRead(**asdict(product)) for product in result]


@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id:int, update_data: ProductUpdate, db:Session=Depends(get_db)):
    product_repository = ProductRepository(db)
    use_case = UpdateProductUseCase(product_repository)
    update_dto = ProductUpdateDTO(**update_data.model_dump())
    result = use_case.execute(product_id, update_dto)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead(**asdict(result))

@router.delete("/{product_id}", response_model=ProductRead)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_repository = ProductRepository(db)
    use_case = DeleteProductUseCase(product_repository)
    result = use_case.execute(product_id)

    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductRead(**asdict(result))



