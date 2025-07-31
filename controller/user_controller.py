from typing import List
from fastapi import HTTPException
from fastapi import APIRouter
from model.user import User
from repository import user_repository

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await user_repository.get_by_id(user_id)      ##### user_service######
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id: {user_id} not found"
        )
    return user


@router.post("/")
async def create_user(user: User):
    print("this is user " + str(dict(user)))
    await user_repository.create_user(user)               ##### user_service######



@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int):
    await user_repository.delete_user(user_id)              ##### user_service######



@router.get("/", response_model=List[User])
async def get_users():
    return await user_repository.get_all()                  ##### user_service######