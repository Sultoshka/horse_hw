import requests

url = 'https://httpbin.org/forms/post'
data = {'custname': 'Elon Musk',
        'custtel': '+9989999999',
        'custemail': 'real-elon@mail.com',
        'size': 'small',
        'topping': 'extra cheese',
        'delivery': '12:00',
        'comments': 'hahahahaha'
        }

print(requests.post(url, data=data))
