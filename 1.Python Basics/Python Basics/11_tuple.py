# tuples are immutable (better for constants)
# faster than lists
# can be used as dict keys

marks = (75,64,73,75,98,45,75)
marks2 = (64,73,98,45,75)

print(marks.count(75))
print(marks.index(73))

print(3*marks) #repitition
print(marks+marks2) #appending