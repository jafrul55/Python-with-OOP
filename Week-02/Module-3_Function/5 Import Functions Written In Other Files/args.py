# def add(num1,num2):
#     total = num1 + num2
#     print(num1,num2)
#     print(f'num1:{num1} and num2:{num2}')
#     return total
# Result = add(12,14)
#result = add(num1 = 12,num2 = 14)


# def multiply(num1,num4,num2=1,num3=1):
#right side default parameter
#     result = num1*num4
#     return result

# output = multiply(30,50)
# print(output)


#-------------------------------
#without write lot of parameter

# def multiply2(*number):
    # print(number)

# final_multiply = multiply2(12,2,3)
# print(final_multiply)


#-------------------------------
def multiply3(*number):  #(*number)is Args
    result = 1
    for num in number:
        result = result *num
    return result

final_result = multiply3(12,2,3,5,6)  #lot of parameter
# print(final_result)


def add(num1,num2,*numbers): 
    #in tuple you can take specific Value
    print(num1,num2)
    print(numbers)

add(3,4,5,6,7)
