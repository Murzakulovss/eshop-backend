from sqlalchemy.orm import Session

from app.models import Product
from app.schemas.product import ProductCreate

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db:Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db:Session, product: ProductCreate, owner_id: int):
    db_product = Product(name = product.name,
                         description = product.description,
                         price = product.price,
                         owner_id=owner_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db:Session, name: str, description: str,price:float, product_id: int):
    product = get_product(db, product_id)
    if not product:
        return None
    product.name = name
    product.description = description
    product.price = price
    db.commit()
    db.refresh(product)
    return product

def delete_product(db:Session, product_id:int):
    product = get_product(db,product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product

