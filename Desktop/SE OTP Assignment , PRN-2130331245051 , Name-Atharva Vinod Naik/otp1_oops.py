import math
import random
import smtplib
from twilio.rest import Client

class OTPGenerator:
    def __init__(self):
        self.DIGITS = "0123456789"
        self.OTP = ""

    def generate_otp(self):
        for _ in range(6):
            self.OTP += self.DIGITS[math.floor(random.random() * 10)]
        return self.OTP

class OTPSender:
    def __init__(self, account_sid, auth_token, twilio_number, target_number):
        self.client = Client(account_sid, auth_token)
        self.TWILIO_NUMBER = twilio_number
        self.TARGET_NUMBER = target_number

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_=self.TWILIO_NUMBER,
            to=self.TARGET_NUMBER
        )
        return message.body

    def send_email(self, subject, body, sender_email, recipient_email, password):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        email_msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, email_msg)
        server.quit()

# Example usage:

# Initialize OTPGenerator and generate OTP
otp_generator = OTPGenerator()
otp = otp_generator.generate_otp()

# Initialize OTPSender with Twilio and email credentials
otp_sender = OTPSender(
    account_sid='ACc90b01dc3b9e5727a207731cb591b9a7',
    auth_token='e82ec90c73f7079a4976d17d09467627',
    twilio_number='+15856394364',
    target_number='+919607614198'
)

# Send OTP via SMS
sms_msg = otp_sender.send_sms(f"{otp} is your otp")
print(sms_msg)

# Send OTP via Email
otp_sender.send_email(
    subject='OTP for Verification',
    body=f'Hello, Your OTP is {otp}',
    sender_email='naikatharva111@gmail.com',
    recipient_email='naikatharva1111@gmail.com',
    password='jbctzddvhpwysdhf'
)
