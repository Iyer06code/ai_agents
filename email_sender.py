import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrets import sender_email, password


def send_email(receiver_email: str, subject: str, content: str) -> str:
    """Send an email to the specified receiver with the given subject and content."""

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(content, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()
        print("✅ Email sent successfully!")
        return "Email sent successfully"
    except Exception as e:
        print("❌ Error:", e)
        return f"Error sending email: {e}"
