from abc import ABC, abstractmethod
from app.domain.models.product import Product
from app.interfaces.schemas.product import ProductUpdate

class ProductRepositoryInterface(ABC):

    @abstractmethod
    def get_by_id(self, product_id:int) -> Product:
        pass

    @abstractmethod
    def create(self, product) -> None:
        pass

    @abstractmethod
    def update(self, product_id:int, update_data: ProductUpdate) -> None:
        pass

    @abstractmethod
    def delete(self, product_id:int) -> None:
        pass