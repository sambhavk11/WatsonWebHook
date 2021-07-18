import numpy as np
from flask import Flask, request, make_response
import json
import requests


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
    URL="https://free.currconv.com/api/v7/convert"
    PARAMS={"q":"SGD_INR","compact":"ultra","apiKey":"7a2db6e45a77e71a05c9"}
    r=requests.get(url=URL,params=PARAMS)
    data=r.json()
    fulfilmentres="the currency conversion for now is " + str(data['SGD_INR'])
    return {"fulfillmentText":fulfilmentres}

if __name__ == '__main__':
    app.run()


    
"""https://free.currconv.com/api/v7/convert?q=USD_SGD&compact=ultra&apiKey=7a2db6e45a77e71a05c9"""