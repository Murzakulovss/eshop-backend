from abc import ABC, abstractmethod
from app.domain.models.product import Product

class ProductRepositoryInterface(ABC):

    @abstractmethod
    def get_dy_id(self, product_id:int) -> Product:
        pass

    @abstractmethod
    def create(self, product) -> None:
        pass

    @abstractmethod
    def update(self, product_id:int) -> None:
        pass

    @abstractmethod
    def delete(self, product_id:int) -> None:
        pass