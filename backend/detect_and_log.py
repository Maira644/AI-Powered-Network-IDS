from feature_extractor import create_feature_vector
from detection_engine import predict_attack

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "database")
    )
)

from alert_logger import save_alert


def detect_flow(flow, source_ip, destination_ip):

    features = create_feature_vector(flow)

    result = predict_attack(features)

    print("\n===== DETECTION RESULT =====")
    print(result)

    if result["prediction"] == "Attack":

        save_alert(
            source_ip=source_ip,
            destination_ip=destination_ip,
            attack_type="Detected Threat",
            risk_score=result["risk_score"],
            severity=result["severity"],
            action=result["action"]
        )

    return result