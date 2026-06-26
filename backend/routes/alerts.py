import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "database")
    )
)

from fastapi import APIRouter
from sqlalchemy import select

from models import engine, alerts

router = APIRouter()

@router.get("/alerts")
def get_alerts():

    with engine.connect() as connection:

        result = connection.execute(
            select(alerts)
        )

        data = []

        for row in result:

            data.append(dict(row._mapping))

        return data