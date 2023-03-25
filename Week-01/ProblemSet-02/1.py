character = input("Input String: ")
result = ""
for Ch in character:
    if Ch.isupper():
        result += Ch.lower()
    else:
        result += Ch.upper()
print(result)