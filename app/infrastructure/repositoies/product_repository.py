from abc import ABC
from sqlalchemy.orm import Session
from app.domain.models import Product
from app.domain.repositories.product_repository_interface import ProductRepositoryInterface
from app.infrastructure.database.models import ProductORM
from app.dto.product import ProductCreateDTO, ProductUpdateDTO

from app.infrastructure.mappers.product_mapper import to_domain

from typing import cast

class ProductRepository(ProductRepositoryInterface, ABC):
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id:int) -> Product | None:
        product_orm = self.db.query(ProductORM).filter(ProductORM.id == product_id).first()
        if not product_orm:
            return None
        return to_domain(cast(ProductORM, product_orm))

    def create(self, product: ProductCreateDTO) -> Product:
        product_orm = ProductORM(
            name=product.name,
            description=product.description,
            price=product.price,
            owner_id=product.owner_id
        )
        self.db.add(product_orm)
        self.db.commit()
        self.db.refresh(product_orm)
        return to_domain(product_orm)

    def update(self, product_id:int, update_data: ProductUpdateDTO) -> Product:
        product_orm = self.db.query(ProductORM).filter(ProductORM.id == product_id).first()
        if not product_orm:
            raise ValueError("Product not found")
        if update_data.name is not None:
            product_orm.name = update_data.name
        if update_data.description is not None:
            product_orm.description = update_data.description
        if update_data.price is not None:
            product_orm.price = update_data.price
        self.db.commit()
        self.db.refresh(product_orm)

        return to_domain(cast(ProductORM, product_orm))

    def delete(self, product_id: int) -> None:
        product_orm = self.db.query(ProductORM).filter(ProductORM.id == product_id).first()
        if not product_orm:
            raise ValueError("Product not found")
        self.db.delete(product_orm)
        self.db.commit()














