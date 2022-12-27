#testing flask here
from flask import Flask,request,redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
from ret_time import *
from scrape import *
# import time


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h> Welcome to our Hospital Bot! </h>"


@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    if len(msg>0):
        csv()

    resp = MessagingResponse()
    resp.message(output(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

