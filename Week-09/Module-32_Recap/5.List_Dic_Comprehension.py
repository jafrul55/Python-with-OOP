#list and dictionary Comprehension:

#list comprehension:
# [expression for item in range()]
#Example -1:
# lst = ["hello","world","python"]
# new_list = [x.upper() for x in lst]
# print(new_list)

#Example -2:

# x = [i for i in range(1,10)]
# print(x)

#Alternative method:
# y = list(range(1,10))
# print(y)

#Example -3:
# string to list convert:
# x = "Hello"
# y = [i for i in x]
# print(y)
# print(list(x))

#Example -4:
# lst = [x for x in range(1,20) if x%2 == 0]
# print(lst)

#Example -5:
# lst = [x for x in range(100) if x%3 == 0 if x%5 == 0]
# print(lst)

#Example -6:
# lst = ["Even" if x%2 == 0 else "Odd" for x in range(100)]
# print(lst)

#Example -7:
# lst = [(x,y) for x in [1,2,5,6,7] for y in [3,4,8,9,10] if x != y]
# print(lst)

#Dictionary Comprehension:
# dct = {key:value for item in range()}
#example -1:
# dct = {i:i+10 for i in range(10)}
# print(dct)

#example -2: if even:
# dct = {'jack': 30,"rahim":22,"karim":21}
# new_dct = {k:v for k,v in dct.items() if v%2 == 0}
# print(new_dct)

# example -3: if bigger than other number

# dct = {'jack': 30,"rahim":22,"karim":21}
# new_dct = {k:v for k,v in dct.items() if v%2 != 0 if v > 18}
# print(new_dct)

#Example -4: check old and young
# dct = {'jack': 60,"rahim":22,"karim":21,'Jafrul':23}

# new_dct = {k:('old' if v >= 50 else 'young') for k,v in dct.items()}
# print(new_dct)

#Example -5: In dictionary we will keep another dictionary
dct = {k1 : {k2: k1*k2} for k2 in range(6) for k1 in range(5)}
print(dct)



