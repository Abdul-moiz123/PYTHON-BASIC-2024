file = open("myfile.txt" , "w")
r = file.write("hello my name is abdul moiz")
print(r)
file.close()

file = open("myfile.txt")
r = file.read()
print(r)
file.close()

file = open("myfile.txt" , "r")
r = file.readline()
print(r)
r1 = file.readline()
print(r1)
r2 = file.readline()
print(r2)
r3 = file.readline()
print(r3)
file.close()

file = open("myfile.txt" , "r")
r = file.readlines()
print(r)
file.close()


with open("myfile.txt") as f:
    print(f.read())