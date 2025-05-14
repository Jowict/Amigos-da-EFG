import requests   

respose = requests.get('https://oeapi.com/api/v2/pokemon')
print(respose.json())