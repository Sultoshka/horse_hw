import requests

link = 'https://icanhazip.com/'
responce = requests.get(link).text
print(responce.status_code)
print(responce.text)