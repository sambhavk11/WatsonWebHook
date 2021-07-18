import numpy as np
from flask import Flask, request, make_response
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'

# geting and sending response to IBM Watson
@app.route('/webhook', methods=['POST'])
def webhook():   
    res = processRequest(request)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-type'] = 'application/json'
    r.headers['Accept'] = 'application/json'
    return r



# processing the request from IBM Watson
def processRequest(req):
    
    number1=1
    number2 =4
    fulfilmentres="the sum is : " + str(number1+number2)
    return {"fulfilmentres":fulfilmentres}

if __name__ == '__main__':
    app.run()

