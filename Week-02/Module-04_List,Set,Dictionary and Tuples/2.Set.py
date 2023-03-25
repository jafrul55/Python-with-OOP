numbers =[12,45,56,45,12,89]
# print(numbers)

#Set(Duplicate value will set one time):
# Set will be unique
nums = {12,45,56,45,12,89}
# print(nums)

numbers_set = set(numbers)
print(numbers_set)
# To add element:
numbers_set.add(77)
numbers_set.add(45)  #duplicate value never add
print(numbers_set)

# you can remove set element:
numbers_set.remove(12)
print(numbers_set)

# you can count set element using len function:
print(len(numbers_set))