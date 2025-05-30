from app.domain.models.product import Product
from app.infrastucture.database.models.product import ProductORM


def to_domain(product_orm: ProductORM) -> Product:
    id = product_orm.id
    name = product_orm.name
    description = product_orm.description
    price = product_orm.price
    owner_id = product_orm.owner_id
    return Product(id=id, name=name,description=description,price=price,owner_id=owner_id)

def from_domain(product: Product) -> ProductORM:
    id = product.id
    name = product.name
    description = product.description
    price = product.price
    owner_id = product.owner_id
    return ProductORM(id=id,name=name,description=description,price=price,owner_id=owner_id)