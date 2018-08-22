import os
import logging
from datetime import datetime, timedelta
import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
riskUrl = os.environ["RISK_URL"]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', risk="")

@app.route('/', methods=['POST'])
def homeOnSubmit():
	riskArray = []
	submittedValue = int(request.form['form-a1c']) * 100
	logging.debug(submittedValue)
	riskArray.append(submittedValue)
	risksJson = json.dumps(riskArray)
	r = requests.post(riskUrl, data=risksJson)
	return render_template('index.html', risk=r.json())
