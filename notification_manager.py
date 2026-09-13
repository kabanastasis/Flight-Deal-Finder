import smtplib, os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = os.environ["EMAIL_ADDRESS"]
        self.password = os.environ["EMAIL_PASSWORD"]
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]

    def send_email(self, email_list, subject, message):
        with smtplib.SMTP(self.smtp_address, 587) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject: {subject}\n\n{message}"
                )
