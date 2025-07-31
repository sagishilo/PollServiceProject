from typing import Optional, List
from model.user import User
from repository.database import database

TABLE_NAME = "users"

async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:user_id"
    result= await database.fetch_one(query, values={"user_id":user_id})
    if result:
        return User(**result)
    return None


async def get_all() -> List[User]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results =await database.fetch_all(query)
    return [User(**result) for result in results]


async def create_user(new_user: User)-> int:
    query= f"""
    INSERT INTO {TABLE_NAME} (first_name,last_name,email,age, address)
    VALUES(:first_name, :last_name, :email, :age, :address)
    """
    values={"first_name": new_user.first_name ,"last_name":new_user.last_name,
            "email":new_user.email, "age":new_user.age, "address":new_user.address}

    async with database.transaction():
        await database.execute(query, values)
        last_record_id=await database.fetch_one("SELECT_LAST_INSERT_ID()")
    return last_record_id[0]


async def register_user(user_id: User)-> int:
    query = f"UPDATE {TABLE_NAME} SET is_registered = TRUE WHERE id= :user_id"
    await database.execute(query, values={"user_id":user_id})



async def update_user(user_id: int, updated_user: User):
    query = f"""
    UPDATE {TABLE_NAME}
    SET first_name = :first_name,
    last_name= :last_name,
    email= :email,
    age= :age
    address= :address
    WHERE id= :user_id
    """
    values={"first_name": updated_user.first_name ,"last_name":updated_user.last_name,
            "email":updated_user.email, "age":updated_user.age, "address":updated_user.address,
            "user_id":updated_user.id}
    await database.execute(query, values)


async def delete_user(user_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id= :user_id"
    values ={"user_id":user_id }
    await database.execute(query, values)


async def is_user_registered(user_id: int) -> bool:
    query = f"SELECT is_registered FROM {TABLE_NAME} WHERE id=:user_id"
    result = await database.fetch_one(query, values={"user_id": user_id})
    if result:
        return True
    return False