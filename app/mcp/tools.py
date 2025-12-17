from sqlalchemy import text
from db.mcp_engine import engine
from db.redis_client import redis_client
import json

def get_user(user_id: int) -> dict:
    cache_key = f"user:{user_id}"

    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    with engine.connect() as conn:
        row = conn.execute(
            text("SELECT id, name, email FROM users WHERE id=:id"),
            {"id": user_id}
        ).fetchone()

    if not row:
        return {"error": "user not found"}

    user = dict(row._mapping)
    redis_client.setex(cache_key, 60, json.dumps(user))
    return user
