class DeleteProductUseCase:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, product_id: int):
        try:
            self.product_repository.delete(product_id)
            return True
        except ValueError:
            return False

