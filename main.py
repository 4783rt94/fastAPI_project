from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User, Gender, Role
from typing import List
from uuid import UUID

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Temporary list simulating a database
db: List[User] = [
    User(id=UUID("9b331d15-0130-4f31-9dc3-1209ac057408"), first_name="Mikael", last_name="Smith", gender=Gender.male, roles=[Role.student]),
    User(id=UUID("7415ba23-3ad4-4e5f-b1ea-bca1b58aa5ac"), first_name="Alice", last_name="Terry", gender=Gender.female, roles=[Role.admin, Role.user])
]

@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/users")
async def fetch_users():
    return db

@app.post("/api/users/register")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"detail": "User deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} does not exists"
    )
