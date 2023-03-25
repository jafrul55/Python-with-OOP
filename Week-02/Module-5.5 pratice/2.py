def calculation(a,b):
    addition = a+b
    subtraction = a - b
    return addition,subtraction
result = calculation(2,3)
print('Sum: ',result[0])
print('Minus: ',result[1])
print(type(result))

# 1.methods:Tuple packing
# def calculation(a, b):
#     add = a + b
#     subtract = a - b
#     return add, subtract

# result = calculation(2, 3)
# print(result) # (5, -1)

#2.methods: list packing
# def calculation(a, b):
#     add = a + b
#     subtract = a - b
#     return [add, subtract]

# result = calculation(2, 3)
# print(result) # [5, -1]

# 3.method:Dictionary packing
# def calculation(a, b):
#     add = a + b
#     subtract = a - b
#     return {'add': add, 'subtract': subtract}

# result = calculation(2, 3)
# print(result) # {'add': 5, 'subtract': -1}



