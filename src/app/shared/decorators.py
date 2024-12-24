from functools import wraps
from fastapi import HTTPException, status
from ..user_management.keycloack_custom import verify_token


# Decorator to extract and verify the token
def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs.get("request")  # Get the request object

        print(request)

        # Get token from query parameter or header
        token = request.query_params.get("token", None) or request.headers.get(
            "Authorization", None
        )

        if not token:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Token is missing"
            )

        if token.startswith("Bearer "):
            token = token[7:]  # Remove "Bearer " if present

        decoded_token = verify_token(token)  # Verify the token
        return await func(
            *args, **kwargs, decoded_token=decoded_token
        )  # Pass decoded token to the endpoint function

    return wrapper
