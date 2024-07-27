########################################## LANBDA FUNCTION ############################################

# add = lambda x , y : x+y
# print(add(2,3))

# square = lambda x : x**2
# print(square(3))

# mode = lambda x : x%2==0
# print(mode(342))

########################################## MAP FUNCTION ############################################
# def make_even(num):
#     if(num%2==1):
#         return num+1
#     else:
#         return num
    
# x = [123,345,345,4321,245,456,678,325,677,55,567,88,644,678]  

# y = list(map(make_even,x))
# print(y)

###########################################  FILTER FUNCTION ##########################################
# avail_units = {
#     '101' : {
#         'bedroom' : 3,
#         'bathroom' : 2,
#         'price' : 1625
#     },
#     '215' : {
#         'bedroom' : 2,
#         'bathroom' : 1,
#         'price' : 1550
#     },
#     '231' : {
#         'bedroom' : 1,
#         'bathroom' : 1,
#         'price' : 1400
#     }
# }

# def with_filter(unit_num):
#     if(avail_units[unit_num]['price'] < 1600 and avail_units[unit_num]['bedroom'] >=2):
#         return True
#     else:
#         return False

# y = list(filter(with_filter , avail_units))
# print(y)

################################################# LIST COMHPERATION ######################################
# nums = [1,2,3,4,5,6,7,8,9,10]
# # square = []
# # for num in nums:
# #     square.append(num**2)
# # print(square)

# # short way to do
# square = list(num**2 for num in nums)
# print(square)

###############################################################################################################