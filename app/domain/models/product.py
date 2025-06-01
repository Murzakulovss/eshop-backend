class Product:
    def __init__(self, product_id: int, name:str, description: str, price: float, owner_id: int):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.owner_id = owner_id
