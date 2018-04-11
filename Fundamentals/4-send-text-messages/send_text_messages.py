from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACffa8dd947c16018706d7ddf230156c65"
# Your Auth Token from twilio.com/console
auth_token  = "63e8a4b91131027bb5082988640065b3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5521996152361", 
    from_="+12542218102",
    body="Hello from Python!")

print(message.sid)