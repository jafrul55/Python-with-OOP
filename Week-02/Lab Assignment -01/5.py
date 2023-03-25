# x = {'a':1,'b':2,'c':3,'d':4}

# result = []
# for key,value in x.items():
#     result.extend([key,value])
# print(result)

# for second one:
# d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

# result1 = []
# for k,v in d.items():
#     result1.extend([k,v])
# print(result1)

# def create_list(x):
#     result = []
#     for key,value in x.items():
#         result.extend([key,value])
#     return result

# x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
# print(create_list(x))


def create_list(d):
    result = []
    for key,value in d.items():
        result.extend([key,value])
    return result

d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
print(create_list(d))