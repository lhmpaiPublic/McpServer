from sqlalchemy import create_engine
import os

engine = create_engine(
    "mysql+pymysql://root:root@mysql:3306/mcp",
    echo=True
)
