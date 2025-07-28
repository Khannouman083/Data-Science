from math import sqrt
num = input("Enter a number to find its square root: ")
num= int(num) #built-in function
print(sqrt(num)) # module function

# uder defined function
def sumfunc(first, second):
    sum=first+second
    return sum

first = input("Enter 1st number for sum: ")
second = input("Enter 2nd number for sum: ")

first=int(first)
second=int(second)
sum=sumfunc(first, second)
print(f"The sum is {sum}")