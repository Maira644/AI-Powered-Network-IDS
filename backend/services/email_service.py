import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT
)


def send_email(subject, body):

    try:

        message = MIMEMultipart()

        message["From"] = EMAIL_ADDRESS
        message["To"] = EMAIL_ADDRESS
        message["Subject"] = subject

        message.attach(
            MIMEText(body, "plain")
        )

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        )

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        server.send_message(message)

        server.quit()

        print("Email sent successfully!")

    except Exception as e:

        print("Email Error:", e)