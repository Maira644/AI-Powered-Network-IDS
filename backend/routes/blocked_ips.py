import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "database")
    )
)

from fastapi import APIRouter
from sqlalchemy import select

from models import engine, blocked_ips

router = APIRouter()


@router.get("/blocked-ips")
def get_blocked_ips():

    with engine.connect() as connection:

        result = connection.execute(
            select(blocked_ips)
        )

        data = []

        for row in result:
            data.append(dict(row._mapping))

    return data