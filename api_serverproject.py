from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

# create fastapi application
app = FastAPI (
    title = "My first api",
    description = "Learning rest apis"
    ,version = "1.0"
)

# Temporary in-memory database
students = {
    1: {"name": "Haresh", "department": "AI & DS"},
    2: {"name": "Arun", "department": "CSE"}
}

#home end point
@app.get("/")
def home ():
    return {"message":"welcome to haresh api"}

#retrive all the students
@app.get("/students")
def get_students():
    return students
# retriving specific students
@app.get("/students/{student_id}")
def get_stud(student_id:int):
    if student_id not in students:
        #now we need to raise an exception
        raise HTTPException(
            status_code = 404,
            detail = "Student not found"
        )
    return students[student_id]

# Query parameter
@app.get("/search")
def search_student(name: str):
    return {"searching_for": name}


# Define expected request body
class Student(BaseModel):
    name: str
    department: str


# POST: Create a student
@app.post("/students")
def create_student(student: Student):

    new_id = max(students.keys(), default=0) + 1

    students[new_id] = student.model_dump()

    return {
        "message": "Student created successfully",
        "student_id": new_id,
        "student": students[new_id]
    }


# DELETE: Remove a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted = students.pop(student_id)

    return {
        "message": "Student deleted",
        "student": deleted
    }
