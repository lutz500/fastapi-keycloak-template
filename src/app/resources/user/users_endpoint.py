from fastapi import APIRouter, Depends, Security, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from ...database import get_async_db
from ...user_management.keycloack_custom import verify_token
from ...shared.decorators import auth_required

router = APIRouter()


@router.get("")
async def get_user(
    db: AsyncSession = Depends(get_async_db), token: dict = Security(verify_token)
):
    result = await db.execute(text("Select * from users;"))
    users = []
    for user in result.all():
        users.append(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password_hash": user.password_hash,
            }
        )
    return users


@router.get("/decorator")
@auth_required
# This function validates the token using the auth_required decorator
# to avoid unnecessary code repetition and unused parameters
async def get_user(request: Request, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(text("Select * from users;"))
    users = []
    for user in result.all():
        users.append(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password_hash": user.password_hash,
            }
        )
    return users
