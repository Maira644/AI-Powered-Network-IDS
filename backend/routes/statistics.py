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


@router.get("/statistics")
def get_statistics():

    with engine.connect() as connection:

        result = connection.execute(
            select(alerts)
        )

        rows = result.fetchall()

    return {
        "total_alerts": len(rows),

        "critical_alerts": sum(
            1 for row in rows
            if row.severity == "Critical"
        ),

        "high_alerts": sum(
            1 for row in rows
            if row.severity == "High"
        ),

        "medium_alerts": sum(
            1 for row in rows
            if row.severity == "Medium"
        ),

        "low_alerts": sum(
            1 for row in rows
            if row.severity == "Low"
        )
    }