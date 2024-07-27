number = int(input("Enter the number: "))
if(number % 2 == 0):
    print("THe number is even")
else:
    print("THe number is odd")


age = int(input("Enter your age: "))
if(age>=18):
    print("You are above the age to drive that good")
elif(age<0):    
    print("You are entering the invalid age")
else:    
    print("You are below the age to drive that bad")