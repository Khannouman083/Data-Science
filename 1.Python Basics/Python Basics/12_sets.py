# unique values are stored in sets 
# no indexes unordered

marks ={46,25,46,87,96,43}
marks2={49,25,24,63,74,73}
print(marks) 

marks.add(37) # adds element
marks.remove(96) #remove element
print(marks)

print(marks | marks2)
print(marks.union(marks2))
print(marks & marks2)
print(marks.intersection(marks2))

print(marks2.issubset(marks))
print(marks.issuperset(marks2))


