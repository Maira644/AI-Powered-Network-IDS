from sqlalchemy import insert
from datetime import datetime

from models import engine, alerts

def save_alert(
    source_ip,
    destination_ip,
    attack_type,
    risk_score,
    severity,
    action
):

    query = insert(alerts).values(
        source_ip=source_ip,
        destination_ip=destination_ip,
        attack_type=attack_type,
        risk_score=risk_score,
        severity=severity,
        action=action,
        timestamp=datetime.now()
    )

    with engine.begin() as connection:
        connection.execute(query)

    print("Alert Saved Successfully")