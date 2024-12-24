from fastapi import APIRouter

from .resources.user import users_endpoint

# Create the API router
api_router = APIRouter()

# Include the resource endpoints
api_router.include_router(users_endpoint.router, tags=["users"], prefix="/users")
