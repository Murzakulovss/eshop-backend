from app.domain.models.product import Product
from app.infrastucture.database.models.product import ProductORM


def to_domain(product_orm: ProductORM) -> Product:
    product_id = product_orm.id
    name = product_orm.name
    description = product_orm.description
    price = product_orm.price
    owner_id = product_orm.owner_id
    return Product(product_id=product_id, name=name, description=description, price=price, owner_id=owner_id)

def from_domain(product: Product) -> ProductORM:
    product_id = product.product_id
    name = product.name
    description = product.description
    price = product.price
    owner_id = product.owner_id
    return ProductORM(id=product_id, name=name, description=description, price=price, owner_id=owner_id)