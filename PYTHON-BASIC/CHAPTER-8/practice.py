# def greatest(a , b , c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
#     elif(a==b==c):
#         return a
#     else:
#         return "invalid"    
# a = int(input("enter the first number: "))    
# b = int(input("enter the second number: "))    
# c = int(input("enter the third number: "))    
# large = greatest(a,b,c)    
# print(large)



# def degree(temp):
#     frah = (temp*(9/5))+32
#     return frah
# temp = degree(int(input("Enter the temperature in ceslius: ")))
# print(temp)



# def recursive(number):
#     if(number==1): # base condition to avoid error in recursion
#         return 1
#     return recursive(number-1) + number 
# number = int(input("enter the number that you want sum of: "))
# print(recursive(number))



# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(3)    


# def in_to_cm(number):
#     return number * 2.54
# n = in_to_cm(int(input("enter the value in inches: ")))
# print(n)




# def rem(li , word):
#     lit = []
#     for name in li:
#         if not (name==word):
#             lit.append(name.strip(word))
#     return lit
    
# li = ["anas" , "momo" , "sonu" , "nu"]
# print(rem(li,"nu"))


# def table(number):
#     if(number>0):
#         for a in range(1,11):
#             print(f" {number} X {a} = {number*a}")
# table(int(input("Enter the number of which you want table: ")))


