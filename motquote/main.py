import smtplib
import datetime as dt
import random
import sys

import ssl
from email.message import EmailMessage

def get_quote():
    day_of_week = dt.datetime.now().weekday()
    print(f"Today is {day_of_week}")
    quotes = []
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()

    return random.choice(quotes)

    
def send_email(quote:str,app_password:str):
    msg = EmailMessage()
    msg["Subject"] = "Quote of the day"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"{quote}")
    # Send via SMTP_SSL (Port 465)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
    
sender_email = "sajit.kunnumkal@gmail.com"
receiver_email = "13jacobkmathew@gmail.com"



if __name__ == "__main__":
    app_password = sys.argv[1]
    quote = get_quote()
    print(f"Todays quote \n {quote}")
    send_email(quote,app_password)

