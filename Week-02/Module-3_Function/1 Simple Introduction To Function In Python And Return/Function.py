def double_it(num):
    result = num * 2
    print(result)

# double_it(50)       #function parameter call


def add(num1,num2):
    total = num1 + num2
    # print(total)
    return total

sum = add(34,45)
print(sum)
# add(45,30)


def multiply(num1,num2):
    result = num1 * num2
    return result

output = multiply(20,40)
print(output)


ultimate = add(sum,output)
print('Final Output',ultimate)