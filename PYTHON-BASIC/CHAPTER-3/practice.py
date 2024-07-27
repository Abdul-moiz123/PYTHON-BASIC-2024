name = input("enter your name: ")
str = f"Good afternoon, {name}"
print(str)

date = "7 june 2024"
str1 = f"Dear {name} \n You are selected \n {date}"
print(str1)

# OR

letter = """
        Hello , |name|,
              You are selected
              |date|
        """
str3 = letter.replace("|name|" , "abdul moiz").replace("|date|" , "6 june 2024")   # you can make chain of str methods
print(str3)


moiz = "hello my name is  abdul  moiz"
print(moiz.find("  ")) # other value if access 
print(moiz.find("rafay")) # -1 value if not found 

rafay = moiz
rafay = rafay.replace("  " , " ")
print(rafay)


letter = "Hello moiz,\n\t You are selected \n 7 june 2024"
