a  = "Phiiiiitron"
# a[0] = 'K'
# b = a.count('i')
# print(a)
# print(b)
# b = a.split('i')
# print(b)
b = list(a)
c = set(b) #set unindex data structure
# c[0] = 'A'
x = {1,2,3,4} #you can not change by indexing
# x.add(5)
x.pop()
x.remove(2)
# print(x)
# print(b)
d = tuple(b)
# d[0] = 'm'
# print(c)
# print(d)

#Now we will talk about Dictionary:
t = [{"name": "rahat","roll":30,"marks":(10,10,20)},
{"name": "rifat","roll":29,"marks":(100,20)}]

# roll = int(input("Enter Input: "))

# for i in t:
#     if i["roll"] == roll:
#         # print(i["marks"])
#         print(f"Student Name: {i['name']} Roll: {i['roll']} marks: {sum(i['marks'])}")

#for Counter:
from collections import Counter
#time complexity = O(n)^2

print(Counter(a))