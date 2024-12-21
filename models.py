from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    __tablename__ = "user"

    username: str = Field(..., min_length=3, description="Має містити мінімум 3 символи")
    email: EmailStr = Field(..., description="Має бути валідною електронною адресою")
    age: int = Field(..., min_age=18, description="Має бути цілим числом більше 18")





class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


products = [
    Product(id=1, name="Laptop", price=1200, in_stock=True),
    Product(id=2, name="Mouse", price=25, in_stock=True),
    Product(id=3, name="Keyboard", price=45, in_stock=False),
    Product(id=4, name="Monitor", price=300, in_stock=True),
]