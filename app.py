from flask import Flask
from twilio.rest import Client
import os
app = Flask(__name__)
client = Client(os.environ['REUN_TWILIO_ACCOUNT_SID'], os.environ['REUN_TWILIO_ACCOUNT_SECRET'])


@app.route('/')
def hello_world():
    return 'App is live!'
    
@app.route('/sms', methods=['POST'])
def text_text():
    # Create a phone call that uses our other route to play a song from Spotify.
    message = client.messages \
                .create(
                     body="test",
                     from_=os.environ['REUN_TWILIO_FROM_NUMBER'],
                     to='+19173735223'
                 )
 
    return str(response)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
