import matplotlib.pyplot as plt

students = ["Arun", "Bala", "Charan", "David"]
marks = [85, 90, 75, 95]

plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance")

plt.show()