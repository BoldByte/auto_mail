import smtplib
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

class EmailSender:
    def __init__(self):
        load_dotenv(".env")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 465  # Use 465 for SSL or 587 for TLS
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.sender_password = os.getenv('SENDER_PASSWORD')

    def send_email(self, receiver_emails, subjects, bodies, file_paths=None):
        if not isinstance(receiver_emails, list):
            receiver_emails = [receiver_emails]
        if not isinstance(subjects, list):
            subjects = [subjects]
        if not isinstance(bodies, list):
            bodies = [bodies]

        if len(receiver_emails) != len(subjects) or len(receiver_emails) != len(bodies):
            raise ValueError("Number of receiver emails, subjects, and bodies must be the same")

        if file_paths is None:
            file_paths = []

        success = False

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.sender_email, self.sender_password)

            for receiver_email, subject, body in zip(receiver_emails, subjects, bodies):
                message = MIMEMultipart()
                message['From'] = self.sender_email
                message['To'] = receiver_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'html'))

                for file in file_paths:
                    part = MIMEApplication(file.read(), Name=file.name)
                    part['Content-Disposition'] = f'attachment; filename="{file.name}"'
                    message.attach(part)

                server.sendmail(self.sender_email, receiver_email, message.as_string())
            success = True
        except Exception as e:
            print(f'Error: {e}')
        finally:
            server.quit()
            return True if success else False



if __name__ == '__main__':
    
    receiver_email = 'donenoelle@gmail.com'

    subject = 'Subject of your email'
    body = """
        Hello!
        This is a beautiful HTML email example.
    """

    email_sender = EmailSender()
    email_sender.send_email(receiver_email, subject, body)
