import requests

endpoint = "http://localhost:8000/api/products/"


data = {
    "title": "this field is done23",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)
