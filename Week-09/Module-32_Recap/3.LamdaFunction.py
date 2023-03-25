# def greet():
#     print('Good Morning')
# greet()

#Lamda Function: anonymouse
# a = lambda arg :expression
# a = lambda : print("Good Morning")
# a()

# Example -1:
# First uppercase and then reverse:

# s = "Phitron"
# new_string = lambda str: str.upper()[::-1]
# print(new_string(s))

#Example -2:
# mx = lambda a,b : a if(a>b) else b
# print(mx(3,4))
# print(mx(6,mx(3,4)))
# print(mx(mx(6,5),mx(3,4)))

#Example -3:
# List_Comprehenssion:
# lst = [1,2,3,4,5,6,7]
# #lamda way:
# new_list = [lambda arg = x : arg*2 for x in lst]
# for i in new_list:
#     print(i())

#Simple way:
# def a(x):
#     return x * 2

# for i in lst:
#     print(a(i))

#Example -4:
#Filter() function:
# my_list = [1,2,3,4,5,6,7,8]
# new_list = list(filter(lambda x: (x%2 == 0),my_list))
# print(new_list)

#Example -5:
#map() function:
# make every string upper:
# string_list = ["hello","world","python"]
# new_list = list(map(lambda x: x.upper(),string_list)) #iterative way
# print(new_list)

#Example -6:
# reduce() function:
# for that you need to from reduce import functools:
lst = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in lst:
#     sum += i
# print(sum)
#we can do it easily using reduce() function:
# reduce function everytime will take two value and will sum
from functools import reduce
sum = reduce(lambda x,y:x+y,lst)
print(sum)




