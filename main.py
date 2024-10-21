from fastapi import FastAPI
from models import User, Gender, Role
from typing import List
from uuid import UUID, uuid4

app = FastAPI()

# Temporary list simulating a database
db: List[User] = [
    User(id=UUID("9b331d15-0130-4f31-9dc3-1209ac057408"), first_name="Mikael", last_name="Smith", gender=Gender.male, roles=[Role.student]),
    User(id=UUID("7415ba23-3ad4-4e5f-b1ea-bca1b58aa5ac"), first_name="Alice", last_name="Terry", gender=Gender.female, roles=[Role.admin, Role.user])
]

@app.get("/")
async def root():
    return {"Hello": "World!"}

@app.get("/api/users")
async def fetch_users():
    return db

@app.post("/api/users/register")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

