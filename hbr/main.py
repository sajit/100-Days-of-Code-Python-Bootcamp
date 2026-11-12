##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import sys

import ssl
from email.message import EmailMessage

def get_message():
    content = None
    with open("letter_templates/letter_3.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print(f"Raw content {content}")
    return content

sender_email = "sajit.kunnumkal@gmail.com"
receiver_email = "sajit.kunnumkal@gmail.com"


def send_email(quote:str,app_password:str):
    msg = EmailMessage()
    msg["Subject"] = "Happy birthday"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"{quote}")
    # Send via SMTP_SSL (Port 465)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

def greeting(password):
    message = get_message()
    message = message.replace("[NAME]",receiver_email)
    send_email(message,password)

if __name__ == "__main__":
    app_password = sys.argv[1]
    greeting(app_password)
