from sqlalchemy import insert
from datetime import datetime

from models import engine, blocked_ips

def save_blocked_ip(
    ip_address,
    reason
):

    query = insert(blocked_ips).values(
        ip_address=ip_address,
        reason=reason,
        blocked_at=datetime.now()
    )

    with engine.begin() as connection:
        connection.execute(query)

    print("Blocked IP Saved Successfully")