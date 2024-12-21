from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI, HTTPException
from models import RegisterRequest

app = FastAPI()

# 1.
users = [
    {"id": 1, "name": "Sasha"},
    {"id": 2, "name": "John"},
    {"id": 3, "name": "Alice"}
]



# 2.
@app.post("/register")
async def register_user(data: RegisterRequest):
    return {
        "message": "Користувач успішно зареєстрований",
        "user": data
    }



# 3.
