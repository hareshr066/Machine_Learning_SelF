# for getting from the api
import requests
# public api endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"
# send http get request
response = requests.get(url)
#print server response
print("Status code:" , response.status_code)
#convert it to python dict
data = response.json()
print("response:",data)

 #=============================================================================================
# for posting the request !

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Learning APIs",
    "body": "I am learning REST APIs with Python",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.json())
#============================================================================================

