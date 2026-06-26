from feature_extractor import create_feature_vector
from detection_engine import predict_attack
from services.email_service import send_email

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "database")
    )
)

from alert_logger import save_alert
from alert_manager import display_alert


def detect_flow(flow, source_ip, destination_ip):

    features = create_feature_vector(flow)

    result = predict_attack(features)
    

    display_alert(
        result,
        source_ip,
        destination_ip
    )

    if result["prediction"] == "Attack":

        save_alert(
            source_ip=source_ip,
            destination_ip=destination_ip,
            attack_type="Detected Threat",
            risk_score=result["risk_score"],
            severity=result["severity"],
            action=result["action"],
            status="New",
            recommendation=result["action"]
        )

        if result["severity"] == "Critical":

            subject = "🚨 Critical Network Attack Detected"

            body = f"""
    Critical Alert!

    Source IP: {source_ip}
    Destination IP: {destination_ip}

    Risk Score: {result['risk_score']}
    Severity: {result['severity']}

    Recommended Action:
    {result['action']}

    AI-Powered Network IDS
    """

        send_email(subject, body)

    return result