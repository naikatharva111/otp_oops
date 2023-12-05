from twilio.rest import Client
import math
import random
import smtplib
account_sid = 'ACc90b01dc3b9e5727a207731cb591b9a7'
auth_token = 'e82ec90c73f7079a4976d17d09467627'

twilio_number = '+15856394364'
target_number = ''
client = Client(account_sid,auth_token)
digits="0123456789" 
otp=""
for i in range(6): 
    otp+=digits[math.floor(random.random()*10)] 
otp = otp + " is your otp" 
msg= otp
message = client.messages.create(
    body = msg,
    from_ = twilio_number,
    to = '+919607614198'
)
print(message.body)

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('naikatharva111@gmail.com','jbctzddvhpwysdhf')
msg='HELLO YOUR OTP IS '+str(otp)
server.sendmail('naikatharva111@gmail.com','naikatharva1111@gmail.com',msg)
server.quit()