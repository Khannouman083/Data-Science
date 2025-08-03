# Artithematic Operators
first = input("Enter a number: ")
second = input ("Enter a second number: ")

first=int(first)
second=int(second)

print(first+second) 
print(first-second) 
print(first*second)
print(first/second)
print(first%second) #remainder
print(first//second) #divide result should be int
print(first**second) #power
print()

# Operator Precedence
exp1 = first * second + second / first
exp2 = first * (first + second) / second
print(exp1)
print(exp2)
print()

# () - Highest precedence
# ** - 2nd
# +x,-x,~x - 3rd
# *,/,//,% - 4th
# -,+ - 5th
# .
# .
# .
# .
# =,+=,-=,*=,/= - Lowest

# Comparison Operators
print(first>second) 
print(second<=first) 
print(first<second) 
print(second>=first) 
print((first!=second)) 
print()

# logical operators
print((first>second) and (first<second)) #false
print((first>second) or (first<second)) #true
print(not(first>second))


