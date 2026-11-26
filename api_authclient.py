import requests

url = "http://127.0.0.1:8000/protected"

headers = {
    "x-api-key": "my-secret-123"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())