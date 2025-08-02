# Random module
import random

print(random.random())         # 0.23423
print(random.randint(1, 10))   # 7
print(random.choice(['cat', 'dog', 'bird']))


# math functions
import math

print(math.sqrt(25))      # 5.0
print(math.pow(2, 3))     # 8.0
print(math.factorial(5))  # 120
print(math.ceil(3.2))     # 4
print(math.floor(3.9))    # 3


# using datetime
from datetime import datetime, timedelta

now = datetime.now()
print("Current:", now)

yesterday = now - timedelta(days=1)
print("Yesterday:", yesterday)

formatted = now.strftime("%d-%m-%Y %H:%M")
print("Formatted:", formatted)


# using requests module
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Headers:", response.headers["content-type"])
print("JSON Data:", response.json())
