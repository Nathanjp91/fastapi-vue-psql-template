""" Hello World Route handler """

from fastapi import APIRouter, Depends
from app.db import get_session
from app.models.users import User
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/")
async def hello_world(session: AsyncSession = Depends(get_session)):
    """Hello World route handler"""
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [users]
