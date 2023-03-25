numbers = [12,45,56,45,12,89]
print(numbers)
# Tuple(is immutable(Oporibortonio))
numbers_tuple = 12,45,56,45,12,89
print(numbers_tuple)

# you can also declare it using ()
nums_tuple = (12,45,56)
# print(nums_tuple)
# you can access in tuple
print(numbers_tuple[0])
print(numbers_tuple[3])
# But you can not assign any value in tuple
# numbers_tuple[2] = 44

# you can not delete any element from tuple:
# del numbers_tuple[1]

# But you can change value if it is mutable
tuple2D = ([12,45,12],[45,11,])
tuple2D[0][2] = 99
tuple2D[1][1] = 121
print(tuple2D)

# this is also a tuple
# short_tuple = 2,

# you can make number all value in tuple
tuple_from_list = tuple(numbers)
print(tuple_from_list)