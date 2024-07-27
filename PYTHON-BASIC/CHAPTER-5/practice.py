dic = {
    "moiz":"aloo",
    "anas":"bagan",
    "rafay":"math"
}
answer = input("enter the words : ")
print(dic[answer])


s = set()
s1= int(input("enter the number: "))
s.add(s1)
s2= int(input("enter the number: "))
s.add(s2)
s3= int(input("enter the number: "))
s.add(s3)
s4= int(input("enter the number: "))
s.add(s4)
s5= int(input("enter the number: "))
s.add(s5)
s6= int(input("enter the number: "))
s.add(s6)
s7= int(input("enter the number: "))
s.add(s7)
s8= int(input("enter the number: "))
s.add(s8)
print(s)

s= set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # it will give 2 as if he value is same its will not look the datatype of value


dic= {}
name = input("Enter the name : ")
lang = input("Enter the language : ")
dic.update({name:lang})
name1 = input("Enter the name : ")
lang1 = input("Enter the language : ")
dic.update({name1:lang1})
name2 = input("Enter the name : ")
lang2 = input("Enter the language : ")
dic.update({name2:lang2})
print(dic.items())