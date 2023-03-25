numbers = [12,45,65,23,89,78,11]

# def get_numbers (nums):
#     return nums

# result = get_numbers(numbers)
# print(result)

# But if we use here a loop:
def get_numbers (nums):
    for num in nums:
        return num

result = get_numbers(numbers)
print(result)
# return has one more version is yield:
print('Generator: ')
def get_numbers(nums):
    for num in nums:
        yield num

result = get_numbers(numbers)
print(next(result))
print(next(result))
print(next(result))
print('I have a generator')
print('I have no idea about genetor')
print(next(result))