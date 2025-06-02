from app.domain.models.product import Product
from app.infrastructure.database.models.product import ProductORM


def to_domain(orm_product: ProductORM) -> Product:
    product_id = orm_product.id
    name = orm_product.name
    description = orm_product.description
    price = orm_product.price
    owner_id = orm_product.owner_id
    return Product(product_id=product_id, name=name, description=description, price=price, owner_id=owner_id)


def from_domain(product: Product) -> ProductORM:
    product_id = product.product_id
    name = product.name
    description = product.description
    price = product.price
    owner_id = product.owner_id
    return ProductORM(id=product_id, name=name, description=description, price=price, owner_id=owner_id)
