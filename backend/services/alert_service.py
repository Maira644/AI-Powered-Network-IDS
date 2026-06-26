import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "database"
        )
    )
)

from sqlalchemy import select

from models import engine, alerts


def get_all_alerts():

    with engine.connect() as connection:

        result = connection.execute(
            select(alerts)
        )

        return [
            dict(row._mapping)
            for row in result
        ]