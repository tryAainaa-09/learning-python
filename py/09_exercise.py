# student = {
#     "name": "Aishah",
#     "age": 20,
#     "grade": "A",
#     "courses": ["Math", "Science", "History"]
# }

#Accessing values in the dictionary
# print(student["name"])
# print(student.get("age"))
# student["age"] = 21             # Updating the age
# student["email"] = "aishah@gmail.com"   #adding a new key-value

#print(student["name"], student["age"], student["grade"], student["courses"])

# keys = student.keys()
# values = student.values()
# items = student.items()
# print(keys)
# print(values)
# print(items)

#nested dictionary
# company = {
#     "employees": {
#         "nana": {"age": 25, "position": "Sales"},
#         "arina" : {"age": 30, "position": "Marketing"},
#         "alex" : {"age": 28, "position": "Engineer"}
#     },
#     "positions": ["Sales", "Marketing", "Engineer"]
# }

# #print(company["employees"].items())  # Accessing nested dictionary value
# print(company["positions"])

#Exercise 9: Dictionary

student_records = {
    "Student_001": {"name": "John", "age": 19, "major": "Computer Science", "grades": [85, 92, 78]},
    "Student_002": {"name": "Sarah", "age": 20, "major": "Biology", "grades": [90, 88, 95]},

}

student_records["Student_003"] = {"name": "Michael", "age": 18, "major": "Mathematics", "grades": [82, 79, 91]}

print(student_records["Student_001"]["name"])  # Accessing nested dictionary value