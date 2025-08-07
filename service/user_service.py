from typing import Optional, List

import httpx
from fastapi import HTTPException

from api.internalApi.user_service import answer_service_api
from model.user import User
from repository import user_repository


async def get_by_id(user_id: int) -> Optional[User]:
    existing_user = await user_repository.get_by_id(user_id)
    if existing_user:
        return existing_user
    else:
        raise ValueError(f"There is no user with id: {user_id}")



async def get_all() -> List[User]:
    return await user_repository.get_all()


async def create_user(new_user: User)-> Optional[int]:
    existing_user = await user_repository.get_by_id(new_user.id)
    if existing_user:
        raise ValueError(f"The user with id: {new_user.id} is already exist")
    else:
        return await user_repository.create_user(new_user)


async def register_user(user_id: int):
    user = await user_repository.get_by_id(user_id)
    if user:
        if user.is_registered:
            raise ValueError(f"The user with id: {user_id} is already registered")
        else:
            return await user_repository.register_user(user_id)
    else:
        raise ValueError(f"There is no user with id: {user_id}")


async def update_user(user_id: int, updated_user: User):
    existing_user = await user_repository.get_by_id(user_id)
    if existing_user:
        if user_id == updated_user.id:
            return await user_repository.update_user(user_id, updated_user)
        else:
            raise ValueError(f"New user id is not valid")
    else:
        raise ValueError(f"There is no user with id: {user_id}")

async def delete_user(user_id: int) -> Optional[str]:
    existing_user = await user_repository.get_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail=f"There is no user with id: {user_id}")

    try:
        await answer_service_api.delete_answers_for_user(user_id)
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Answer service returned error: {e.response.text}"
        )
    await user_repository.delete_user(user_id)
    return f"The user with id {user_id} was deleted"



async def is_user_registered(user_id: int) -> Optional[bool]:
    existing_user = await user_repository.get_by_id(user_id)
    if existing_user:
        return await user_repository.is_user_registered(user_id)
    raise ValueError(f"There is no user with id: {user_id}")

