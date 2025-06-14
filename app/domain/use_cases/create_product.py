from app.dto.product import ProductCreateDTO

class CreateProductUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, name: str, description: str, price: float, owner_id: int):
        product = ProductCreateDTO(
            name=name,
            description=description,
            price=price,
            owner_id=owner_id
        )
        return self.product_repository.create(product)

