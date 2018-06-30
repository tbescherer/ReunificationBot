from flask import Flask, request, session
from twilio.rest import Client
import os
app = Flask(__name__)
app.secret_key = os.environ['REUN_FLASK_SECRET_KEY']
client = Client(os.environ['REUN_TWILIO_ACCOUNT_SID'], os.environ['REUN_TWILIO_ACCOUNT_SECRET'])


@app.route('/')
def hello_world():
    return 'App is live!'
    
@app.route('/sms', methods=['POST'])
def text_text():
    session['counter'] = session.get('counter', 0) + 1
    app.logger.info(session['counter'])
    app.logger.info(request.form)
    message = client.messages \
                .create(
                     body="test",
                     from_=os.environ['REUN_TWILIO_FROM_NUMBER'],
                     to='+19173735223'
                 )
    
    return str('empty')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
