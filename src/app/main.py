from fastapi import FastAPI

from .api import api_router
from .core import settings

# Create the FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Include the API routes
app.include_router(api_router, prefix=settings.API_V1_STR)
