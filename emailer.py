import os, smtplib

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

GOOGLE_APP_PASSCODE = os.getenv("GOOGLE_APP_PASSCODE")

from_email = 'vipinreyo.test@gmail.com'
to_email = 'vipinreyo.test@gmail.com'
body = """Hello, this is a message from a python smtp email client"""

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login('vipinreyo.test@gmail.com', GOOGLE_APP_PASSCODE)
smtp_server.sendmail(from_email, to_email, body)
smtp_server.quit()
print('Email sent successfully')

