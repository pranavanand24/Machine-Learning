# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:58:34 2019

@author: pranav anand
"""

from twilio.rest import Client

account_sid = "AC0c746d9ce656ea51746ef54a8752e66c"
auth_token = " 05a16a71ce6f7c7aee8a2031c8a3f9e7 "

client = Client(account_sid ,auth_token)

message= client.messages \
               .create(
        body ="my name is lord voldemort",
        from_='+17014013297',
        to = '+911234567890'
         
        )
        
print(message.sid)
