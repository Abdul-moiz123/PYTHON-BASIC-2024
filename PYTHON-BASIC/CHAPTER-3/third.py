# first = 'moiz'
#         #0123
#     #   -4-3-2-1
# second = "moiz"
# third = """moiz"""


# print(first)
# print(second)
# print(third)

# print(len(first))

# print(first[:]) # will be 0 and len always
# print(first[:4]) # will be 0 always
# print(first[0:4]) # 0 1 2 3  --> excluise 4 
# print(first[1:2]) # 1  --> excluise 2

# print(first[::-1])
# print(first[::1]) # leave 0 character
# print(first[::2]) # leave 1 character
# print(first[::3]) # leave 2 character
# print(first[::4]) # leave 3 character
# print(first[::34563]) # give starting charcter 
# print(first[::-34563]) # give ending charcter 
# print(first[-3:-1])  # check the positive slicing in case to identify negative slicing -3 means 1 and -1 means 3 --> oi

# FUNCTION OF STRING

str = "moiz a is boy"
print(len(str))
print(str.endswith("boy"))
print(str.startswith("moiz"))
print(str.capitalize())
print(str.title())
print(str.lower())
print(str.upper())
print(str.zfill(23))
print(str.find("b"))
print(str.count("o"))
print(str.replace("m" , "p"))
print(str.isalnum())
print(str.isalpha())
print(str.isascii())
print(str.isdecimal())
print(str.isidentifier())
print(str.islower())
print(str.isnumeric())
print(str.isspace())
print(str.istitle())
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print(str.index("o"))
print(str.removeprefix("moiz"))
print(str.removesuffix("boy"))
print(str.casefold())
print(str.center(23))
print(str.expandtabs(2))
