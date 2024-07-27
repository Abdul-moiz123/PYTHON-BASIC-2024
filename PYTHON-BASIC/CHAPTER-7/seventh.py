# WHILE LOOP

i = 1
while(i<11):
    print(i)
    i+=1

li = ["moiz","nafay","aqsa","abdullah","sonu","momo","anas","rafay","haseeb"]
a = 0
while(a<len(li)):
    print(li[a].capitalize())
    a+=1

i = 11
while(i<51):
    print(i)
    i+=1


# FOR LOOP

for a in range(6):
    print(a)
print()

for b in range(0,6):
    print(b)
print()

for c in range(0,6,2):
    print(c)
print()

str = "abdulmoiz"
for a in str:
    print(a)
print()    
li = ["moiz","nafay","aqsa","abdullah","sonu"]
for b in li:
    print(b)
print()    
tp = ("moiz","nafay","aqsa","abdullah")
for c in tp:
    print(c)
print()    


# BREAK  CONTINUE  PASS

for a in range(1,6):
    if(a==3):
        break
    print(a)
print()    

for b in range(1,6):
    pass
print()    

for c in range(1,6):
    if(c==3):
        continue
    print(c)
print()    

