from fastapi import FastAPI, HTTPException
from utils import users, register_user
from models import products

app = FastAPI()


# 1.
@app.get("/users")
async def get_users():
    return users



# 2.
@app.post("/register")
async def register_user():
    return register_user



# 3.
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Продукт не знайдено")