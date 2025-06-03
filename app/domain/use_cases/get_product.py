class GetProductUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, product_id: int):
        if not product_id:
            return None
        return self.product_repository.get_by_id(product_id)
