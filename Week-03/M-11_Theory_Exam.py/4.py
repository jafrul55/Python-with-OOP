def sort_string(str):
    string = ""
    for i in range(len(str)):
        if i % 2 != 0:
            num = int(str[i])
            for val in range(num):
                string += str[i-1]
    return string


input_string = 'x3b4U5i2'
val = sort_string(input_string)
val2 = ''.join(sorted(val,key=str.casefold))
print(val2)
