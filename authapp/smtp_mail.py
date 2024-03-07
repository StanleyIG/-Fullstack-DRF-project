from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


SMTP_USER = os.getenv('EMAIL')
SMTP_PASSWORD = os.getenv('PASSWORD')
SMTP_HOST = "smtp.yandex.ru"
SMTP_PORT = 465

def send_verification_email_task(url):
    html = f"""
    send mail registrtion
    """
    msg = EmailMessage()
    msg.set_content(html)
    msg['Subject'] = 'Reset Password'
    msg['From'] = SMTP_USER
    msg['To'] = url

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)


# send_verification_email_task('oootehts@gmail.com', 1)