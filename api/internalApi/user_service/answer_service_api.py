from fastapi import HTTPException
from config.config import Config
import httpx

from service import user_service

config= Config()

async def count_answers_for_user(user_id: int):
    url=f"{config.ANSWER_API_BASE_URL}/{user_id}/user_votes_count"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"User service returned error: {e.response.text}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal error while calling user service: {str(e)}"
            )


async def delete_answers_for_user(user_id: int):
    url = f"{config.ANSWER_API_BASE_URL}/{user_id}/user_votes"
    async with httpx.AsyncClient() as client:
        response = await client.delete(url)
        response.raise_for_status()
        return response.json()

