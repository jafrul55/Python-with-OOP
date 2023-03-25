#list:
# lst = [1,2,3,4,[5,6,[7,8,[11,12,[13,14]]]]]

# print(1 in lst)
# print(lst[4][2][2][2][0])
# lst.append(100)
# lst.append([1,2,3])
# print(lst)

# lst[4][2][2][2][0] = 13*2
# print(lst)


#tuple:
#you can change index inside the tuple:
# tp = (1,2,3,4,5,[1,2,3,4])
# 'tuple' object does not support to access value
# tp[0]=4
# tp[5][0] = 13
# print(tp[5][0])

#Dictionary:
# dct = {"rahim" : 12000,"karim":20000}
# print(dct["rahim"])
# print(dct["halim"]) #to handel this error
# print(dct.get('halim')) #None
#you can also print False:
# print(dct.get("halim",False)) #False

# child1 = {
#     "name":"jack",
#     "year": 2002
# }

# child2 = {
#     "name":"emilia",
#     "year":2004
# }

# child3 = {
#     "name":"tom",
#     "year":1999
# }

# myfamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3
# }

# print(myfamily)
# print(myfamily["child2"]["year"])
# print(myfamily.get("child2",False).get("year",False))

#To convert List_of_Tuple to Dictionary:
a = dict([(1,'A'),(2,'B'),(3,'C'),(4,'D')])
# print(a)
# a.pop(3)
# print(a)
# print(a.keys())
# print(a.values())

# for key,value in a.items():
#     print(f"Key {key} : Value {value}")

#Set:
#Never take Duplicate value,unorder datastructure:
st = {1,2,2,3,4,5}
# print(st)
#unorder data structure so not accessable as order
# print(st[0])
# st.insert(0,3) #Not Insertable
# print(st)

#String:
# s = "3 I love Bangladesh"
s = "23333"
# print(s)
#To reverse string:
# print(s[::-1])
#index wise character not changeable
# s[0] = 'i'
# print(s)
#To do uppercase:
# print(s.upper())
#To do lowercase:
# print(s.lower())
#to check wheather value available or not:
# print('I' in s)
# print(s[0].isalpha())
print(s.isalnum())

