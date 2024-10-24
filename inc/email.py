from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib

SMTP_SERVER = os.getenv('SMTP_SERVER', '')
SMTP_PORT = os.getenv('SMTP_PORT', '')
EMAIL = os.getenv('EMAIL', '')
PASSWORD = os.getenv('PASSWORD', '')
TO_EMAIL = os.getenv('TO_EMAIL', '')
FROM_NAME = os.getenv('FROM_NAME','')

def send_email(subject, body):
    """Function to send an email."""
    msg = MIMEMultipart()
    msg['From'] = f"{FROM_NAME} <{EMAIL}>"
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL, TO_EMAIL, text)
    server.quit()