
import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. GET home endpoint
response = requests.get(f"{BASE_URL}/")

print("HOME:", response.status_code)
print(response.json())


# 2. GET all students
response = requests.get(f"{BASE_URL}/students")

print("\nALL STUDENTS:")
print(response.json())


# 3. GET one student
response = requests.get(f"{BASE_URL}/students/1")

print("\nSINGLE STUDENT:")
print(response.json())


# 4. Search using query parameter
response = requests.get(
    f"{BASE_URL}/search",
    params={"name": "Haresh"}
)

print("\nSEARCH:")
print(response.json())


# 5. POST a new student
new_student = {
    "name": "Kumar",
    "department": "ECE"
}

response = requests.post(
    f"{BASE_URL}/students",
    json=new_student
)

print("\nCREATE:")
print(response.status_code)
print(response.json())


# 6. DELETE a student
response = requests.delete(f"{BASE_URL}/students/3")

print("\nDELETE:")
print(response.status_code)
print(response.json())
