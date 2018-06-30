from flask import Flask, request, session
from twilio.rest import Client
import os
from chat import QUESTIONS, ANSWER_TEMPLATE
app = Flask(__name__)
app.secret_key = os.environ['REUN_FLASK_SECRET_KEY']
client = Client(os.environ['REUN_TWILIO_ACCOUNT_SID'], os.environ['REUN_TWILIO_ACCOUNT_SECRET'])


@app.route('/')
def hello_world():
    return 'App is live!'
    
@app.route('/sms', methods=['POST'])
def text_text():
    stage = session.get('stage', 'HELP')
    if session.get('answers') is None:
        session['answers'] = ANSWER_TEMPLATE
    app.logger.info(stage)
    app.logger.info(request.form)

    if QUESTIONS[stage]['collect_answer']:
        session['answers'][stage] = request.form['Body']
    question_message = QUESTIONS[stage]["question"]
    next_stage = QUESTIONS[stage]["following_stage"]
    client.messages.create(
        body=question_message,
        from_=os.environ['REUN_TWILIO_FROM_NUMBER'],
        to='+19173735223'
    )
    session['stage'] = next_stage
    app.logger.info(session['answers'])
    return str('empty')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
