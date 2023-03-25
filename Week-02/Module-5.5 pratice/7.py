# simple_dict = {'a':100,'b':200,'c':300}

# value = 100

# if value in simple_dict.values():
#     print('present')
# else:
#     print('not present')

# you can also use 'any' function to find:
simple_dict2 = {'a':100,'b':200,'c':300}

value = 100

if any(val == value for val in simple_dict2.values()):
    print('present')
else:
    print('not present')

