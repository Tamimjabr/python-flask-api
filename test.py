import requests

BASE_URL = 'http://127.0.0.1:5000/'

response = requests.get(BASE_URL + "videos/5")
print(response.json(), response.status_code)

response2 = requests.post(BASE_URL + "videos/5", {
    "likes": 10,
    "name": "tamim",
    "views": 100
})
print(response2.json(), response2.status_code)

response3 = requests.get(BASE_URL + "videos/5")
print(response3.json(), response3.status_code)

response4 = requests.delete(BASE_URL + "videos/5")
print(response4, response4.status_code)
