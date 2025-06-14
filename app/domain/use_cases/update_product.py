from app.domain.models import Product
from app.dto.product import ProductUpdateDTO, ProductReadDTO


class UpdateProductUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, product_id:int, update_data: ProductUpdateDTO):
        if not product_id:
            return None
        existing_product = self.product_repository.get_by_id(product_id)
        if not existing_product:
            return None
        return self.product_repository.update(product_id,update_data)

