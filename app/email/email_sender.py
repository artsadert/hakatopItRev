import smtplib

from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

password = str(os.getenv("GMAIL_PWD"))
port = 587
sender = "artursadertdinov"
receiver = "k98030118@gmail.com"

async def send(photo_path):
    req_path = os.path.abspath("../email/request.txt")
    #msg = MIMEMultipart('alternative')
    msg = EmailMessage()
    with open(req_path, 'r') as file:
    #    text = MIMEText(file.read(), 'plain')
        msg.set_content(file.read())
    with open(photo_path, 'rb') as file:
        msg.add_attachment(file.read(), maintype='image', subtype='jpg')
    #img = MIMEImage(file.read(), name=os.path.basename(photo_path))
    msg["From"] = sender
    msg["To"] = receiver
    msg['Subject'] = f"Ложный социальный ценник"
    #msg.attach(text)
    #msg.attach(img)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.yandex.ru', port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender, password)
        server.auth_plain()
        server.send_message(sender, receiver, msg)
