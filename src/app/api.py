from fastapi import APIRouter

from .resources.user import users_endpoint

api_router = APIRouter()

api_router.include_router(users_endpoint.router, tags=["users"], prefix="/users")
