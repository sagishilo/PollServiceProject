from typing import List
from fastapi import HTTPException
from fastapi import APIRouter
from model.user import User
from service import user_service

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    try:
        return await user_service.get_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[User])
async def get_users():
    try:
        return await user_service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/")
async def create_user(user: User):
    try:
        print("this is user " + str(dict(user)))
        return await user_service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_id}", response_model=str)
async def delete_user(user_id: int):
    try:
        return await user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    try:
        return await user_service.update_user(user_id, updated_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{user_id}/register", response_model=User)
async def register_user(user_id: int):
    try:
        return await user_service.register_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}/is_register", response_model=bool)
async def is_user_registered(user_id: int):
    try:
        return await user_service.is_user_registered(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))