from fastapi import Header
from fastapi import HTTPException
import secrets
API_KEY = "my-secret-123"

def verify_api_key(x_api_key: str = Header()):

    if not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return True