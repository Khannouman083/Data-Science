with open(r"Exercise.txt", "r") as f:
    data=f.read()

newData=data.replace("C++", "Python")
print(newData)

with open(r"Exercise.txt", "w") as f:
    f.write(newData)