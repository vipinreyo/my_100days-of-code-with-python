import os, smtplib

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

GOOGLE_APP_PASSCODE = os.getenv("GOOGLE_APP_PASSCODE")

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_email = "vipinreyo.test@gmail.com"
to_email = "vipinreyo.test@gmail.com"

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'This is a mail from the SMTP mail python script'

body = """ Hello, this is a friendly message from the SMTP mail python script. You Rock!!!"""

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login('vipinreyo.test@gmail.com', GOOGLE_APP_PASSCODE)

text = msg.as_string()
smtp_server.sendmail(from_email, to_email, text)
smtp_server.quit()

print('Email sent successfully...')