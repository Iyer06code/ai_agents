import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password

def send_email(receiver_email,subject,content):

    subject = subject
    body = "Hello 👋\nThis email was sent using Python!"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(content)
    message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
    server.quit()
    print("✅ Email sent successfully!")

    send_email(receiver_email="4mh23cs129a@gmail.com",subject="Test Email from Python",content="Hello 👋\nThis email was sent using Python!")

except Exception as e:
    print("❌ Error:", e)
