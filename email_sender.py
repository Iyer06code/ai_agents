import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, receiver_email, password


subject = "Test Email from Python"
body = "Hello 👋\nThis email was sent using Python!"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
    server.quit()
    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)
