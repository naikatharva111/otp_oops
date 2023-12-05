import math
import re
import random
import smtplib
from twilio.rest import Client

class OTPGenerator:
    def generate_otp(self):
        digits = "0123456789"
        length = len(digits)
        otp = ""

        for _ in range(6):
            otp += digits[math.floor(random.random() * length)]

        return otp

class Validator:
    @staticmethod
    def validate_mobile(phone_no):
        regex = r'(0|91)?[6-9][0-9]{9}'
        return bool(re.search(regex, phone_no))

    @staticmethod
    def validate_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return bool(re.search(regex, email))

class OTPSender:
    def __init__(self, account_sid, auth_token, twilio_number):
        self.client = Client(account_sid, auth_token)
        self.TWILIO_NUMBER = twilio_number

    def send_otp_over_mobile(self, sent_phone_no, sent_otp):
        message = self.client.messages.create(
            body="Your 6 digit OTP is " + sent_otp,
            from_=self.TWILIO_NUMBER,
            to='+91' + str(sent_phone_no),
        )
        print(message.body)

    def send_otp_over_email(self, sent_email, sent_otp):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
        email_message = 'Your 6 digit OTP is ' + str(sent_otp)
        server.sendmail('naikatharva111@gmail.com', sent_email, email_message)
        server.quit()

# Example usage:

# Initialize OTPGenerator
otp_generator = OTPGenerator()

# Initialize Validator
validator = Validator()

# Initialize OTPSender with Twilio credentials
otp_sender = OTPSender(
    account_sid='ACc90b01dc3b9e5727a207731cb591b9a7',
    auth_token='4e9aaa48cbdd9aac7dc4a1f7a6c09c99',
    twilio_number='+15856394364'
)

# Get user input for phone number and email
input_phone_no = input("Enter the number:")
input_email = input("Enter the Email:")

# Validate and get valid phone number
valid_phone_no = input_phone_no if validator.validate_mobile(input_phone_no) else input("Enter a valid mobile number:")

# Validate and get valid email
valid_email = input_email if validator.validate_email(input_email) else input("Enter a valid email:")

# Generate and send OTP
generated_otp = otp_generator.generate_otp()
otp_sender.send_otp_over_mobile(valid_phone_no, generated_otp)
otp_sender.send_otp_over_email(valid_email, generated_otp)
