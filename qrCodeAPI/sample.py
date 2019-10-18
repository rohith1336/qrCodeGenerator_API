import requests

url = "https://codzz-qr-cods.p.rapidapi.com/getQrcode"

querystring = {"type":"text","value":"Rohith"}

headers = {
    'x-rapidapi-host': "codzz-qr-cods.p.rapidapi.com",
    'x-rapidapi-key': "4bcb1f0648msh1eba11bdcce2652p169a20jsn6caa2c61d81a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
