import requests
import os

response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)
    pass

print(f"Значення змінної IT_TEST = {os.environ['IT_TEST']}")
