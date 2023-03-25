numbers = [12,45,65,23,89,78,11,10]
#to get sum of all numbers use sum function
# total = sum(numbers)
# print(total)

# for List sum:
# total = 0
# for num in numbers:
#     total += num
#     print(num)
# print('Total Sum of list: ',total)

# for Set sum:
# nums = {12,45,56,45,12,89}
# total = 0
# for num in nums:
#     total += num
# print('Total sum of set: ',total)

# for Tuple sum:
# numbers_tuple = 12,45,56,45,12,89
# total = 0
# for num in numbers_tuple:
#     total += num

# print('Total sum of Tuple: ',total)

# for Dictionary sum:
marks = {'physics':12,'chemistry':45,'math':56}
# total = 0
# for mark in marks.values():
#     # print(mark)
#     total += mark

# print('Total sum of Dictionary Value: ',total)

# we can see the value and key using for loop
# for mark in marks:
#     val = marks[mark]
    # print(mark,val)

# Alternative Option:
# for subject,mark in marks.items():
#     print(subject,mark)


# for getting index and value from list using enumerate funation:
for num in enumerate(numbers):
    print(num)

# Alternative:
for i,num in enumerate(numbers):
    print(i,num)

country = 'Bangladesh'
for char in country:
    print(char)