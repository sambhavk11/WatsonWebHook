import numpy as np
from flask import Flask, request, make_response
import json
import requests
from forex_python.converter import CurrencyRates


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'

# geting and sending response to IBM Watson
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-type'] = 'application/json'
    r.headers['Accept'] = 'application/json'
    return r



# processing the request from IBM Watson
def processRequest(req):
    
    
    result = req.get("queryResult")
    #user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    FromCurrency=parameters.get("FromCurrency")
    ToCurrency= parameters.get("ToCurrency")
    c = CurrencyRates()
    conversion=str(c.get_rate(FromCurrency, ToCurrency))[:5]
    
	 
    intent = result.get("intent").get('displayName')
    
    
    #number1=1
    #number2 =4
    #URL="https://free.currconv.com/api/v7/convert"
    #PARAMS={"q":queryCouple,"compact":"ultra","apiKey":"7a2db6e45a77e71a05c9"}
    #r=requests.get(url=URL,params=PARAMS)
    #data=r.json()
    fulfilmentres="The currency conversion for now from " + FromCurrency + " to " + ToCurrency +" is "+ conversion
    return {"fulfillmentText":fulfilmentres}

if __name__ == '__main__':
    app.run()


    
"""https://free.currconv.com/api/v7/convert?q=USD_SGD&compact=ultra&apiKey=7a2db6e45a77e71a05c9"""