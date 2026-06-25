import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(
    os.path.join(BASE_DIR, "ml", "models", "model.pkl")
)

protocol_encoder = joblib.load(
    os.path.join(BASE_DIR, "ml", "models", "protocol_encoder.pkl")
)

service_encoder = joblib.load(
    os.path.join(BASE_DIR, "ml", "models", "service_encoder.pkl")
)

flag_encoder = joblib.load(
    os.path.join(BASE_DIR, "ml", "models", "flag_encoder.pkl")
)

print("Detection Engine Loaded Successfully")

def get_severity(risk_score):

    if risk_score >= 90:
        return "Critical"

    elif risk_score >= 70:
        return "High"

    elif risk_score >= 40:
        return "Medium"

    return "Low"


def calculate_risk(prediction):

    if prediction == 1:
        return 95

    return 10


def predict_attack(features):

    prediction = model.predict([features])[0]

    risk_score = calculate_risk(prediction)

    severity = get_severity(risk_score)

    return {
        "prediction": "Attack" if prediction == 1 else "Normal",
        "risk_score": risk_score,
        "severity": severity,
        "action": "Recommend Blocking"
                  if prediction == 1
                  else "Allow Traffic"
    }