import math
import re
import random
import smtplib
from twilio.rest import Client

class OTPGenerator:
    @staticmethod
    def generate_otp():
        digits = "0123456789"
        length = len(digits)
        return ''.join(random.choice(digits) for _ in range(6))

class UserInputValidator:
    @staticmethod
    def validate_mobile(phone_no):
        regex = r'(0|91)?[6-9][0-9]{9}'
        return bool(re.search(regex, phone_no))

    @staticmethod
    def validate_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return bool(re.search(regex, email))

    @staticmethod
    def get_valid_input(prompt, validator_func):
        while True:
            user_input = input(prompt)
            if validator_func(user_input):
                return user_input
            print("Invalid input. Please try again.")

class OTPSender:
    def __init__(self, account_sid, auth_token, twilio_number, otp_generator):
        self.client = Client(account_sid, auth_token)
        self.twilio_number = twilio_number
        self.otp_generator = otp_generator

    def send_otp(self, recipient, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=self.twilio_number,
            to=recipient,
        )
        print(message.body)

    def send_otp_over_mobile(self, sent_phone_no):
        generated_otp = self.otp_generator.generate_otp()
        message_body = f"Your 6 digit OTP is {generated_otp}"
        self.send_otp(f'+91{sent_phone_no}', message_body)

    def send_otp_over_email(self, sent_email):
        generated_otp = self.otp_generator.generate_otp()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
        email_message = f'Your 6 digit OTP is {generated_otp}'
        server.sendmail('naikatharva111@gmail.com', sent_email, email_message)
        server.quit()

def main():
    otp_generator = OTPGenerator()
    input_validator = UserInputValidator()

    otp_sender = OTPSender(
        account_sid='ACc90b01dc3b9e5727a207731cb591b9a7',
        auth_token='01ff4b225bc6f12d54bb991add7e0275',
        twilio_number='+15856394364',
        otp_generator=otp_generator
    )

    user_phone_no = input_validator.get_valid_input("Enter the number:", input_validator.validate_mobile)
    user_email = input_validator.get_valid_input("Enter the Email:", input_validator.validate_email)

    otp_sender.send_otp_over_mobile(user_phone_no)
    otp_sender.send_otp_over_email(user_email)

if __name__ == "__main__":
    main()
