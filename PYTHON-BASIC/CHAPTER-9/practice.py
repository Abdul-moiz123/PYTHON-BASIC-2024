import random




#  QUESTION 1
# file = open("myfile.txt" , "r")
# content = file.read()
# if("moiz" in content):
#     print("Yes it contain moiz in it")
# else:
#     print("No it does not contain moiz in it")
# file.close()


#   QUESTION 2
# def game():
#     print("Welcome! to the guess game.....")
#     random_score = random.randint(1,60)
#     with open("myHighScore.txt") as f:
#         my_high_score = f.read()
#         if(my_high_score!=""):
#             my_high_score = int(my_high_score)
#         else:
#             my_high_score = 0    
#     print(f"Your high score is {my_high_score}")
#     if(random_score>my_high_score or my_high_score==""):
#         with open("myHighScore.txt" , "w") as f:
#             f.write(str(random_score))
#     return random_score
# print(game())


#   QUESTION 3
# def table(a):
#     tab1 = ""
#     for b in range(1,11):
#         tab1 += f" {a} X {b} = {a*b}\n"
#     with open(f"tables/table_{a}.txt" , "w") as f:
#         f.write(tab1)    

# for c in range(2,21):
#     table(c)


#   QUESTION 4
# word = "Donkey"
# with open("file.txt" , "r") as f:
#     content = f.read()
#     contentNew = content.replace(word, "######")
# with open("file.txt" , "w") as f:
#     f.write(contentNew)    


#   QUESTION 5
# words = ["donkey" , "bad" , "evil"]
# with open("file.txt" , "r") as f:
#     content = f.read()
#     for word in words:
#         content = content.replace(word, "#"*len(word))
# with open("file.txt" , "w") as f:
#     f.write(content)    


#   QUESTION 6
# with open("log.txt" , "r") as f:
#     content = f.read()
# if("python" in content):
#     print("Yes")
# else:
#     print("No")


#   QUESTION 7
# line_no = 1
# with open("log.txt" , "r") as f:
#     lines = f.readlines()
# for line in lines:
#     if("python" in line):
#         print(f"Yes and Line no is {line_no}")
#         break
#     line_no +=1
# else:
#     print(f"Yes and Line no is {line}") 


#   QUESTION 8
# with open("this.txt" , "r") as f:
#     content = f.read()
# with open("mymoiz.txt" , "w") as m:
#     m.write(content)
    

#   QUESTION 9
# with open("this.txt" , "r") as f1:
#     content1 = f1.readlines()
# with open("mymoiz.txt" , "r") as f2:
#     content2 = f2.readlines()
# if(content1 == content2):
#     print("yes")
# else:
#     print("NO")    


#   QUESTION 10
# with open("file.txt" , "w") as f:
#     f.write("")


#   QUESTION 11
with open("old.txt" , "r") as f1:
    content1 = f1.read()
with open("new.txt" , "w") as f2:
    f2.write(content1)
