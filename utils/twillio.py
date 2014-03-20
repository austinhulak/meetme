from twilio.rest import TwilioRestClient
#from flask import Flask, request, redirect
#import twilio.twiml

# =======================================================================================
# Your Account Sid and Auth Token from twilio.com/user/account
#account_sid = "ACeacb9e41c0735e96c88c96dc6176b984"
#auth_token  = "4b56d7ab4d6baa39619d7637ec5f578f"

# -- Austin's paid account:
account_sid = ""
auth_token = ""

# -- phone s
origin_phone = "+18053954222"

DEBUG = True

# =======================================================================================

def send_text(msg, phone_to, phone_from = origin_phone):
    ''' send_text(msg, phone_to, phone_from = origin_phone)
    '''
    client = TwilioRestClient(account_sid, auth_token)
 
    phone_to = clean_phone_number(phone_to)
    message = client.sms.messages.create(body = msg,
                                         to = phone_to,    # Replace with your phone number
                                         from_ = phone_from) # Replace with your Twilio number
    
    if (DEBUG):
        print('Message sent! [%s]' % message.sid)
        print(message)
    
    return message.sid

# =======================================================================================

def clean_phone_number(phone_number):
    if (phone_number[0:2] != '+1'):
        phone_number = '+1%s' % phone_number
    
    return phone_number 
 
# =======================================================================================
 
def get_message(msg_sid):
    client = TwilioRestClient(account_sid, auth_token)
    sms = client.sms.messages.get(msg_sid)
    
    if (DEBUG):
        print('%s\t%s\t%s\n' % (sms.date_sent, sms.body, sms.status))
    
    return sms
 
# =======================================================================================
 
def get_messages():
    client = TwilioRestClient(account_sid, auth_token)

    msgs = []
    for sms in client.messages.list():
        if (DEBUG):
            print('%s\t%s\t%s\t%s\n' % (sms.date_sent, sms.to, sms.body, sms.status))

        msgs.append(sms)
    
    return msgs

# =======================================================================================
 
#@app.route("/", methods=['GET', 'POST'])
#def message_routing():
#    """Respond and greet the caller by name."""
# 
#    from_number = request.values.get('From', None)
#    if from_number in callers:
#        message = callers[from_number] + ", thanks for the message!"
#    else:
#        message = "Monkey, thanks for the message!"
# 
#    resp = twilio.twiml.Response()
#    resp.message(message)
# 
#    return str(resp)
 
 # =======================================================================================

if (__name__ == '__main__'):
    phone_to = "+18056366145" # nick
    phone_to= '8186423789' # roberto
#    phone_to = '5592816656' # austin
#    phone_to = '18052201066' #nick-twillio

    msg = "(twillio works w00t!)"
    msg_sid = send_text(msg, phone_to)
    
    get_messages()
#    get_message(msg_sid)
#    app = Flask(__name__)
#    app.run(debug=True)
    
