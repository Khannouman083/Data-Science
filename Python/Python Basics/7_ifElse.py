age=input("enter your Age: ")
age=int(age)

if(age>=18):
    print("You are an adult")
elif(age>3 and age<18):
    print("You go to school or college")
elif(age>0 and age<3):
    print("Your are a baby")
else: 
    print("Invalid Age")
    