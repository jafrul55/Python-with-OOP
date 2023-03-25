# def square(x):
#     return x * x

# result = square(6)
# print(result)

# we can also make a function using lambda:
square = lambda x: x*x

result = square(6)
print(result)

# you can do sum,multiply,division using lambda

add = lambda x , y: x + y
sum = add(45,56)
# print('Sum of lambda',sum)

# You can double list value by 2 multiply:
numbers = [12,45,65,23,89,78,11]

# you can do it using two way
# def double_it(x):
#     return x*2

# double_it2 = lambda x : x * 2

# for double_it function
# doubled_numbers = map(double_it,numbers)
# print(numbers)
# print(list(doubled_numbers))

# for double-it2 function:
# doubled_numbers2 = map(double_it2,numbers)
# print(numbers)
# print(list(doubled_numbers2))

# you can do it with write lambda outside:
# doubled_numbers = map(lambda x: x*2,numbers)
# print(numbers)
# print(list(doubled_numbers))

# for square same value:
# doubled_numbers2 = map(lambda x: x * x,numbers)
# print(numbers)
# print(list(doubled_numbers2))

# we will use filter for filter value as our wish:

big_numbers = filter(lambda num: num>50,numbers)

print(numbers)
print(list(big_numbers))

# you can use filter in dictionary to find big or small age:
actors = [
        {'name':'Jafrul','age':34},
        {'name':'manna','age':50},
        {'name':'sabana','age':65},
        {'name':'bubli','age':30},
        ]
senior_artists = filter(lambda actor: actor['age']>35,actors)
junior_artists = filter(lambda actor: actor['age']<35,actors)

print(list(senior_artists))
print(list(junior_artists))

