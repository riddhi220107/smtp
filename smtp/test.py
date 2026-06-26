import smtplib
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "riddhimanjrekar2201@gmail.com"
SENDER_PASSWORD = "xppm pagr exvh wshi"  # Use App Password for Gmail

RECEIVER_EMAIL = "prianshetty06@gmail.com"

# Create email
subject = "Test Email"
body = "Hello! This is a test email sent using Python SMTP."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL

try:
    # Connect to SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure the connection
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    # Send email
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)

finally:
    server.quit()