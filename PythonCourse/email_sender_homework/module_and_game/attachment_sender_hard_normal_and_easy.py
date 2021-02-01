import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

to_whom = input("Please write whole email of receiver: ")
subject = "Email with blackjack game and information sender script"
body = "Please place it in on folder because blackjack imports from sender"
sender_email = 'hhttajapai@gmail.com'
receiver_email = to_whom
password = "Breathe1337!"


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email


message.attach(MIMEText(body, "plain"))

filename = "module_and_game.7z"


with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)


part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)


message.attach(part)
text = message.as_string()


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

