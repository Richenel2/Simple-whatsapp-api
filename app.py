from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 
app = Flask(__name__)


@app.route("/")
def help():
    account_sid = 'AC195cf76c0d725909794c30f9b0c32961' 
    auth_token = '70531f5d14ec79c14254cf7fdfb40bad' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body="Salut Yvan, S'il te plait j'ai besoin de ton aide en urgence;",      
                                to='whatsapp:+237696527034' 
                            ) 
    
    print(message.sid)


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {} \n *Kayra Dev* ".format(msg))
    
    account_sid = 'AC195cf76c0d725909794c30f9b0c32961' 
    auth_token = '70531f5d14ec79c14254cf7fdfb40bad' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=msg,      
                                to='whatsapp:+237696527034' 
                            ) 
    
    print(message.sid)
    return str(resp)


if __name__ == "__main__":
    app.run(threaded=True)
