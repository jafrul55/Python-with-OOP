N = input('String: ')
uppercase = 0
lowercase = 0
digit = 0
symbol = 0

for s in N:
    if s.isupper():
        uppercase+=1
    elif s.islower():
        lowercase+=1
    elif s.isdigit():
        digit += 1
    else:
        symbol += 1
print('Uppercase:',uppercase)
print('Lowercase: ',lowercase)
print('Digit: ',digit)
print('Symbol: ',symbol)

