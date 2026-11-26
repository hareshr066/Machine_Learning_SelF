
import requests

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

try:
    # Always set a timeout in real applications
    response = requests.get(url, timeout=5)

    # Raises an exception for HTTP errors (4xx and 5xx)
    response.raise_for_status()

    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.ConnectionError:
    print("Could not connect to the server!")

except requests.exceptions.RequestException as e:
    print("Other request error:", e)
