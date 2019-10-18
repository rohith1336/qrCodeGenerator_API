from flask import Flask, request, url_for, redirect, render_template
import json
import requests
app = Flask(__name__)
url = "https://codzz-qr-cods.p.rapidapi.com/getQrcode"
querystring = {"type":"text","value":""}
headers = {
    'x-rapidapi-host': "codzz-qr-cods.p.rapidapi.com",
    'x-rapidapi-key': "4bcb1f0648msh1eba11bdcce2652p169a20jsn6caa2c61d81a"
    }

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		querystring['value']=request.form['userinput']
		response = requests.request("GET", url, headers=headers, params=querystring)
		print(response.text)
		responseDict=json.loads(response.text)
		return render_template('index.html', qrcode=responseDict['url'], message=responseDict['Message'])
	if request.method == 'GET':
		return render_template('index.html')
