# To find largest number:
largest = max(45,89,54,116,-12)
# print(largest)

# to get max value from set:
num = {12,45,56,45,12,89}
big_num = max(num)
# print(big_num)

# to get min value from set:
num = {12,45,56,45,12,89}
small_num = min(num)
# print(small_num)

# To reverse a list using reverse build_in function:
numbers = [12,45,65,23,89,78,11]
num_reverse = reversed(numbers)
# print(list(num_reverse))

# To make sorted a list numbers in Asscending order:
sorted_number = sorted(numbers)
# print(list(sorted_number))

#Decending order: reverse = True
sorted_number = sorted(numbers,reverse=True)
# print(list(sorted_number))

# to make a dictionary sorted use sorted function:
actors = [
        {'Name':'Sakib Khan','age':34},
        {'Name':'Salman Khan','age':54},
        {'Name':'Sharuk Khan','age':52},
        {'Name':'Solaiman Khan','age':23},
        {'Name':'Tita Khan','age':29}
        ]

sorted_actors = sorted(actors,key = lambda actor:actor['age'])
# print(sorted_actors)
# to make sorting reverse in dictionary:
sorted_actors = sorted(actors,key = lambda actor:actor['age'],reverse=True)
# print(sorted_actors)

# For sorted string:
Friends = ['Kabir','Dabul','Kabul','Motin','Badol','Arian']
sorted_friend = sorted(Friends)
print(sorted_friend)

# reverse string sorted :
Friends = ['Kabir','Dabul','Kabul','Motin','Badol','Arian']
sorted_friend  = sorted(Friends,reverse=True)
print(sorted_friend)
