String = input('s = ')
new_str = ""
str = String.split()
for i,words in enumerate(str):
    new_str += words[::-1]
    if i < len(str)-1:
        new_str += ' '
print('output:',new_str)