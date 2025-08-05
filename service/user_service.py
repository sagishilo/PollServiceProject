from typing import Optional, List
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
        await user_repository.create_user(new_user)


async def register_user(user_id: int):
    user = await user_repository.get_by_id(user_id)
    if user.is_registered:
        raise ValueError(f"The user with id: {user_id} is already registered")
    else:
        return await user_repository.register_user(user_id)


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
    if existing_user:
        await user_repository.delete_user(user_id)
        return f"The user with id {user_id} was deleted"
    else:
        raise ValueError(f"There is no user with id: {user_id}")



async def is_user_registered(user_id: int) -> Optional[bool]:
    existing_user = await user_repository.get_by_id(user_id)
    if existing_user:
        return await user_repository.is_user_registered(user_id)
    raise ValueError(f"There is no user with id: {user_id}")

