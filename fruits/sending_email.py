import smtplib
from email.message import EmailMessage

# Email details
sender_email = "eeumairali@gmail.com"
receiver_email = "rebeliumtemp@gmail.com"
subject = "Hello"
body = "Hello, this is a test email sent using Python!"



# Gmail SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Your Gmail credentials
your_password = "qcss cpuc pkek ulgv"  # Use App Password if 2FA is enabled
messages = ['i am happy','~i am sad','where are you','i was waiting ','~byeeeeee']
for subject in messages:
    # Create email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)
# Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, your_password)
            
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)