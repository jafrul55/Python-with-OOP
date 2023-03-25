# Odd Number ==> after dividing by 2,the remainder will be 1
# Evan Number ==> after dividing by 2,the remainder will be 0
# For Evan
num = 7
while num <= 20:
    num = num + 1
    if num % 2 == 1:
        continue
    print(num)