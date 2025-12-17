from mcp.server.fastapi import FastMCP

mcp = FastMCP("docker-mcp-server")

@mcp.tool()
def get_user(user_id: int):
    """Get user info from database"""
    return {"user_id": user_id, "name": "Alice"}

@mcp.resource("mysql://users")
def users_resource():
    return "User table resource"

@mcp.prompt()
def user_summary(name: str):
    return f"Summarize information about user {name}"
