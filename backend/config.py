import os
from dotenv import load_dotenv

load_dotenv()


# Database

DATABASE_URL = "postgresql://postgres:Ma86jtg0@localhost:5432/network_ids"


# Email

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# Risk Thresholds

LOW_RISK = 20
MEDIUM_RISK = 50
HIGH_RISK = 75
CRITICAL_RISK = 90


# Project

PROJECT_NAME = "AI-Powered Network IDS"
PROJECT_VERSION = "1.0.0"