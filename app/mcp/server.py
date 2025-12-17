from fastapi import APIRouter, HTTPException
from mcp.tools import get_user

router = APIRouter()

@router.post("/tool/get_user")
async def get_user_tool(payload: dict):
    user_id = payload.get("user_id")

    if user_id is None:
        raise HTTPException(status_code=400, detail="user_id is required")

    return get_user(user_id)


