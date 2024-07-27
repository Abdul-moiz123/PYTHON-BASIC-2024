#
# num1 = int(input("Enter the numerator: "))
# num2 = int(input("Enter the demonenator: "))
# try:
#     result = num1/num2
#     print(result)
# except ZeroDivisionError:    
#     print("Opps! You tried to divide by zero")    

#    
# try:
#     result = 20/0
# except FileNotFoundError:
#     print("Opps! File not found that you searching")
# except ZeroDivisionError:
#     print("Opps! You divide with zero")
# except ArithmeticError:
#     print("Opps! You are using wrong arithematic")    

#
# file = None
# try:
#     file = open("sample.txt" , "r")
#     content = file.read()
# except FileNotFoundError:
#     print("Opps! File not found")
# else:
#     print("The content of the file is: \n" , content)
# finally:
#     if file:
#         file.close()
#     print("Program end!!")        

#
# def check_age(age):
#     if(age < 0):
#         raise ValueError("Age cannot be in negative")
# try:
#     check_age(-22)
# except ValueError as ve:
#     print(ve)

##########################################################################################################################

