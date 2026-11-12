import sys
import smtplib
import ssl
from email.message import EmailMessage

sender_email = "sajit.kunnumkal@gmail.com"
receiver_email = "13jacobkmathew@gmail.com"



def main(arg: str):
    app_password = arg
    msg = EmailMessage()
    msg["Subject"] = "Test Email from Python"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Hello! This email was sent using Python's smtplib.")
    # Send via SMTP_SSL (Port 465)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


if __name__ == "__main__":
    main(sys.argv[1])
