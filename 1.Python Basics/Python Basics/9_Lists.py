# collection of item (complex data type)

marks = [98,96,99,68,"Maths"]
print(marks[2])
print(marks[-1])
print(marks[1:4])

marks.append("Physics")
print(marks)
print()

marks.insert(1,"Chemisrty")
print(marks)
print()

print(len(marks))
print()

for item in marks:
    print(item)
print()

i=0
while(i<len(marks)):
    print(marks[i])
    i=i+1
print()

marks.clear()
print(marks)