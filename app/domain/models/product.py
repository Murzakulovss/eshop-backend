class Product:
    def __init__(self, id: int, name:str, description: str, price: float, owner_id: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.owner_id = owner_id
