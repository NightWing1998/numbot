# **********PART 1***************
from flask import Flask,request,jsonify,make_response
import json
import requests

url = 'http://numbersapi.com/'

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return "Hello from Dhruvil Shah"

# ************PART 2**************
@app.route('/',methods=['POST'])
def post():
	req = request.get_json(silent = True,force = True)
	# print(req.get('queryResult'))
	intent = req.get('queryResult').get('intent').get('displayName')
	if( intent == 'Default Welcome Intent'):
		return jsonify({'fulfillmentText':"Welcome"})
	elif(intent == 'numbers'):
		params = req.get('queryResult').get('parameters')
		num = str(int(params.get('number')))
		tempType = params.get('type')
		new_url = url + num + "/" + tempType + "?json"
		# print(new_url)
		reply = requests.get(new_url).json()["text"]
		return jsonify({'fulfillmentText':reply})
		

if( __name__ == '__main__'):
	app.run(debug=True)
