import math
import random
import smtplib
from twilio.rest import Client

class OTPGenerator:
    def generate_otp(self):
        digits = "0123456789"
        length = len(digits)
        otp_value = ""

        for _ in range(6):
            otp_value += digits[math.floor(random.random() * length)]

        return otp_value

class OTPSender:
    def __init__(self, account_sid, auth_token, twilio_number):
        self.client = Client(account_sid, auth_token)
        self.TWILIO_NUMBER = twilio_number

    def send_otp_over_mobile(self, phone_no, otp):
        message = self.client.messages.create(
            body=f"Your 6-digit OTP is {otp}",
            from_=self.TWILIO_NUMBER,
            to=f'+91{phone_no}',
        )
        print(message.body)

    def send_otp_over_email(self, email, otp):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
        email_message = f'Your 6-digit OTP is {otp}'
        server.sendmail('naikatharva111@gmail.com', email, email_message)
        server.quit()

class UserInputValidator:
    @staticmethod
    def validate_mobile(input_phone_no):
        return len(input_phone_no) == 10

    @staticmethod
    def validate_email(input_email):
        return "@gmail.com" in input_email

    @staticmethod
    def get_valid_mobile():
        phone_no_value = input("Enter the number:")
        return phone_no_value if UserInputValidator.validate_mobile(phone_no_value) else input("Enter a valid number")

    @staticmethod
    def get_valid_email():
        email_value = input("Enter the Email:")
        return email_value if UserInputValidator.validate_email(email_value) else input("Enter a valid email")

# Example usage:

# Initialize OTPGenerator
otp_generator = OTPGenerator()

# Initialize OTPSender with Twilio credentials
otp_sender = OTPSender(
    account_sid='ACc90b01dc3b9e5727a207731cb591b9a7',
    auth_token='4e9aaa48cbdd9aac7dc4a1f7a6c09c99',
    twilio_number='+15856394364'
)

# Initialize UserInputValidator
input_validator = UserInputValidator()

# Get and validate user input for mobile and email
user_phone_no = input_validator.get_valid_mobile()
user_email = input_validator.get_valid_email()

# Generate OTP
generated_otp = otp_generator.generate_otp()

# Send OTPs
otp_sender.send_otp_over_mobile(user_phone_no, generated_otp)
otp_sender.send_otp_over_email(user_email, generated_otp)
