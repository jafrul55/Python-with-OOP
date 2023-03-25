import numpy as np
one_d = np.array([1,2,3,4,5,6])
two_d = np.array([[3,5],[5,6],[8,1]])
three_d = np.array([
    [[3,5],[5,6],[8,1]],
    [[3,5],[5,6],[8,1]],
    [[3,5],[5,6],[8,1]]
])

# shaped = one_d.reshape(2,3)
shaped = one_d.reshape(3,2)
changed = np.flip(shaped)

add = two_d + changed
mul = two_d * changed

# back_to_one = mul.flatten().max()
back_to_one = mul.flatten()
print(back_to_one.dtype)
diff_type = back_to_one.astype('f')
print(diff_type.dtype)
print(diff_type)
back_to_one_again = np.copy(back_to_one)
sorted = np.sort(back_to_one_again)
print(sorted)
print(np.sort(three_d))


#to know two dimentional datatype:
# print(two_d.dtype)

#to know shape:
# print(three_d.shape)
# print(two_d.shape)

#to know dimension:
# print(three_d.ndim)

#to know size:
# print(two_d.size)
# print(three_d.size)


# print(back_to_one)
# print(mul)
# print(add)

# print(changed)
# print(shaped)
# print(one_d)
# print(two_d)
# print(three_d)
