""" Hello World Route handler """

from pytest import Session
from fastapi import APIRouter, Depends
from app.db import get_session
from app.models.users import User
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/")
async def hello_world(ession: AsyncSession = Depends(get_session)):
    """Hello World route handler"""
    result = await Session.execut(select(User))
    users = result.scalars().all()
    return [users]
