numbers = [12,45,65,23,89,78,11]

odd_numbers = []
for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

# print(odd_numbers)

# But you can do lot of work using one line for loop:
odd_numbers2 = [num for num in numbers]
# print(odd_numbers2)

# you can multiply 2 using num * 2
odd_numbers2 = [num*2 for num in numbers]
# print(odd_numbers2)

# you can easily find odd number:
odd_numbers3 = [num for num in numbers if num % 2 == 1]
# print(odd_numbers3)

# if num % 5 == 0 want to find:
odd_numbers4 = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
# print(odd_numbers4)

# You can do it for dictionary:
names = ['Sakib','sabbir','salman']
ages = [37,32,21]

pairs = [(name,age) for name in names for age in ages]
print(pairs)

# you can add one mode condition between two loop
pairs1 = [(name,age) for name in names for age in ages if age<25]
print(pairs1)

# alternative:
for name in names:
    print(name)
    for age in ages:
        if age < 25:
            print(name,age)