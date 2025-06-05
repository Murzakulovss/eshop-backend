class GetAllProductsUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, skip: int = 0, limit: int = 100):
        return self.product_repository.get_all(skip = skip, limit=limit)

