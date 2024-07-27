list = [ "moiz" , 56 , True , 33.33 , [2,3,4,5] , (2,4,6,8) , {"moiz":"boy"}]
#        string   int  bool   float    list        tuple             dic

list[0] = "abdullah"
list[3] = 99.989767

print(list[:])
print(list[0:7])
print(list[0:])
print(list[:7])
print(list[1:4])
print(list[::2])
print(list[-4:-1])
print(list[1:678]) # return full list
print(list[1:-678]) # return empty list
print(list[678]) #error index out of bound

# LIST METHODS --> list will change

list.append("moye moye")
print(list)

list1 = [1,2345,4345,67,898,7675,345,3]
list1.sort()
print(list1)
list1.reverse()
print(list1)

list.insert(1, 5678976)
print(list)

list.pop()
print(list)
list.pop(2)
print(list)

list1.remove(1)
print(list1)

list.clear()
print(list)

list.copy()
print(list)

list.extend(list1)
print(list)

list.count("abdullah")
print(list)

print(list.index("abdullah"))



#################################################################################################################################

tp = ("moiz" , 56 , True , 33.33 , [2,3,4,5] , (2,4,6,8) , {"moiz":"boy"} , 5665677)
tp1 = (1),   # tuple of one element we used ,
tp2 = ()

print(tp[:])
print(tp[0:8])
print(tp[0:])
print(tp[:8])
print(tp[1:4])
print(tp[::2])
print(tp[-4:-1])
print(tp[1:678]) # return full list
print(tp[1:-678]) # return empty list
# print(tp[678]) #error index out of bound


concat = tp = tp1
print(concat)

repaet = tp1 * 5
print(repaet)

check = 56 in tp
print(check)

no1 = min(tp)
no2 = max(tp)
print(no1 , no2)


# TUPLE METHODS
tp1= tp.count(1)
print(tp1)
tp2=tp.index(78)
print(tp2)