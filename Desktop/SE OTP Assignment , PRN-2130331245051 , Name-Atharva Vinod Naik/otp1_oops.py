import math
import re
import random
import smtplib
from twilio.rest import Client

class OTPGenerator:
    """
    Class for generating OTPs.
    """
    def generate_otp(self):
        """
        Generate a 6-digit OTP.

        Returns:
            str: The generated OTP.
        """
        digits = "0123456789"
        length = len(digits)
        otp = ""

        for _ in range(6):
            otp += digits[math.floor(random.random() * length)]

        return otp

class UserInputValidator:
    """
    Class for validating user input.
    """
    @staticmethod
    def validate_mobile(phone_no):
        """
        Validate the given mobile number.

        Args:
            phone_no (str): The mobile number to be validated.

        Returns:
            bool: True if the mobile number is valid, False otherwise.
        """
        regex = r'(0|91)?[6-9][0-9]{9}'
        return bool(re.search(regex, phone_no))

    @staticmethod
    def validate_email(email):
        """
        Validate the given email address.

        Args:
            email (str): The email address to be validated.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return bool(re.search(regex, email))

    @staticmethod
    def get_valid_mobile():
        """
        Get and validate the mobile number from the user.

        Returns:
            str: The validated mobile number.
        """
        phone_no_value = input("Enter the number:")
        return phone_no_value if UserInputValidator.validate_mobile(phone_no_value) else input("Enter a valid mobile number")

    @staticmethod
    def get_valid_email():
        """
        Get and validate the email address from the user.

        Returns:
            str: The validated email address.
        """
        email_value = input("Enter the Email:")
        return email_value if UserInputValidator.validate_email(email_value) else input("Enter a valid email")

class OTPSender:
    """
    Class for sending OTPs.
    """
    def __init__(self, account_sid, auth_token, twilio_number, otp_generator, input_validator):
        self.client = Client(account_sid, auth_token)
        self.twilio_number = twilio_number
        self.otp_generator = otp_generator
        self.input_validator = input_validator

    def send_otp_over_mobile(self, sent_phone_no):
        """
        Send OTP to the provided mobile number using Twilio.

        Args:
            sent_phone_no (str): The recipient's mobile number.
        """
        generated_otp = self.otp_generator.generate_otp()
        message = self.client.messages.create(
            body=f"Your 6 digit OTP is {generated_otp}",
            from_=self.twilio_number,
            to=f'+91{sent_phone_no}',
        )
        print(message.body)

    def send_otp_over_email(self, sent_email):
        """
        Send OTP to the provided email address using SMTP.

        Args:
            sent_email (str): The recipient's email address.
        """
        generated_otp = self.otp_generator.generate_otp()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
        email_message = f'Your 6 digit OTP is {generated_otp}'
        server.sendmail('naikatharva111@gmail.com', sent_email, email_message)
        server.quit()

# Example usage:

# Initialize OTPGenerator and UserInputValidator
otp_generator = OTPGenerator()
input_validator = UserInputValidator()

# Initialize OTPSender with Twilio credentials, OTPGenerator, and UserInputValidator
otp_sender = OTPSender(
    account_sid='ACc90b01dc3b9e5727a207731cb591b9a7',
    auth_token='4e9aaa48cbdd9aac7dc4a1f7a6c09c99',
    twilio_number='+15856394364',
    otp_generator=otp_generator,
    input_validator=input_validator
)

# Get and validate user input for mobile and email
user_phone_no = input_validator.get_valid_mobile()
user_email = input_validator.get_valid_email()

# Generate and send OTP
otp_sender.send_otp_over_mobile(user_phone_no)
otp_sender.send_otp_over_email(user_email)
