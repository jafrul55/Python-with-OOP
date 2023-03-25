# S1 = input('String1: ')
# S2 = input('String2: ')
# set1 = set(S1)
# set2 = set(S2)

# if set1.issubset(set2):
#     print(True)
# else:
#     print(False)


# Alternative Option:
Str1 = input('String1: ')
Str2 = input('String2: ')

for S in Str1:
    if(S != Str2):
        print(False)
        break
else:
    print(True)
    

