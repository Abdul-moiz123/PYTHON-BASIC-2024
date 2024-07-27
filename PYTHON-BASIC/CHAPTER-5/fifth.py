dict = {} # empty dict

dic = {
    "moiz":"boy",
    "aqsa":"girl",
    "arham":"boy"
}

print(type(dic))
print(dic)
print(dic["moiz"])
print(dic["aqsa"])
# print(dic["wahab"]) # return error

# DICT METHODS

print(dic.get("moiz"))
print(dic.get("wahab")) # return None not error

dic.update({"marium":"woman" , "moiz":"man"})
print(dic)

print(dic.keys())

print(dic.values())

print(dic.items())

print(dic.pop("moiz"))

print(dic.popitem())


######################################################################################################################

set1 = {1,2,4,5,6,8,5,4,2,4,6,7,4,34,6,6,5}  # if value get repeated it will still take it as single value time
print(type(set1))
print(set1)

empty = set() # empty set --> not this set{}

set2 = {7,45,3,6,74,6,}

set1.add(566)
print(set1)
set1.remove(1)
print(set1)
set1.pop()
print(set1)
s = set1.union(set2)
print(s)
s = set1.intersection(set2)
print(s)
set2.discard(7)
print(set2)

