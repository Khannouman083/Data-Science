my_dict = {
    "name": "Nouman",
    "age": 22,
    "city": "Peshawar"
}

# printing and adding/ modifyng elements
print(my_dict["name"])
my_dict["age"] =21
my_dict["country"] = "Pakistan"
print(my_dict)

# create an empty dictionary
empt_dic = dict() 
print(empt_dic)

# useful methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

del my_dict["country"]
my_dict.pop("name", None) # safe delete and no error if not found
print(my_dict)


# # Practical Example
# # Student records
# students = {
#     "101": {
#         "name": "Ali",
#         "age": 17,
#         "class": "10th",
#         "grades": {
#             "Math": 85,
#             "Science": 90
#         }
#     },
#     "102": {
#         "name": "Sara",
#         "age": 16,
#         "class": "9th",
#         "grades": {
#             "Math": 92,
#             "Science": 88
#         }
#     }
# }

# # display a student record
# student_id= input("Enter a student id: ")
# if student_id in students:
#     student = students[student_id]
#     print("Name:", student["name"])
#     print("Age:", student["age"])
#     print("Class:", student["class"])
#     print("Math Grade:", student["grades"]["Math"])
# else:
#     print("Student not found!")

# # adding a nwe record
# students["103"] = {
#     "name": "Nouman",
#     "age": 18,
#     "class": "12th",
#     "grades": {
#         "Math": 88,
#         "Science": 84
#     }
# }

# # Safe delete (no error if not found)
# students.pop("102", None)  
