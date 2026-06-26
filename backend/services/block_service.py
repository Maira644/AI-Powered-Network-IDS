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

from sqlalchemy import select, insert
from datetime import datetime

from models import engine, blocked_ips


def get_blocked_ips():

    with engine.connect() as connection:

        result = connection.execute(
            select(blocked_ips)
        )

        return [
            dict(row._mapping)
            for row in result
        ]


def block_ip(ip_address, reason):

    query = insert(blocked_ips).values(
        ip_address=ip_address,
        reason=reason,
        blocked_at=datetime.now()
    )

    with engine.begin() as connection:
        connection.execute(query)

    return {
        "message": "IP blocked successfully",
        "ip_address": ip_address
    }