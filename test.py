import requests

BASE_URL = 'http://127.0.0.1:5000/'

response = requests.get(BASE_URL + "helloworld/tamim")
print(response.json())


response2= requests.post(BASE_URL + "helloworld/tamim", {
    "likes": 10,
    "name": "tamim",
    "views": 100
})
print(response2.json())