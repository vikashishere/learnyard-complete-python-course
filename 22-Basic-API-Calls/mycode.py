# ✅ Example 1: GET Request to Public API
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())


# ✅ Example 2: Sending Query Parameters
url = "https://api.agify.io"
params = {"name": "Vikash"}

response = requests.get(url, params=params)

print(response.json())
# Output: {'name': 'Vikash', 'age': 26, 'count': 1234}


# ✅ Example 3: Handling Bad Requests
response = requests.get("https://httpbin.org/status/404")

if response.status_code == 200:
    print("Success!")
else:
    print("Something went wrong:", response.status_code)


# ✅ Example 4: POST Request
url = "https://httpbin.org/post"
data = {"username": "vikash", "score": 90}

response = requests.post(url, json=data)

print(response.json())
