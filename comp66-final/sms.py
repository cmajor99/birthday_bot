#Ryan Steele - 4291461
import os
from twilio.rest import Client

#Traditionally you would not store this hard coded, but env vars were not 
#catching the os.envrion.get() so I had to hard code for demenstration
def sendSMS(fname,phone):
    account_sid = 'AC70bf6b73b2df56cab45c025c803519ff'
    auth_token = '75791d0e431d8d429c87d8b8c6a95a29'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=f"Happy birthday {fname}! I hope you have a wonderful day!",
                        from_='+18137013272',
                        to='+'+ phone
                    )
    print(message)