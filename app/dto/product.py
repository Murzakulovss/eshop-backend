from dataclasses import dataclass

from typing_extensions import Optional

@dataclass
class ProductBase:
    name: str
    price: float
    description: Optional[str] = None

@dataclass
class ProductCreateDTO:
    name: str
    price: float
    owner_id: int
    description: Optional[str] = None

@dataclass
class ProductReadDTO:
    id: int
    name: str
    price: float
    owner_id: int
    description: Optional[str] = None

@dataclass
class ProductUpdateDTO:
    name: Optional[str]
    description: Optional[str]
    price: Optional[float] = None



