from twilio.rest import Client
from credentials import *

client = Client(account_sid, auth_token)

my_msg = "Murodali qalesan dusim"

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)