from fastapi import APIRouter
from models.user import User
from database import users_collection

router = APIRouter()


@router.post("/register")
def register_user(user: User):
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}
