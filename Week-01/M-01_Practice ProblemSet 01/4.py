bool = True
while bool:
   user = input('Take input: ')
   if user == 'Quit':
    # print('Stop the program')
    break
   else:
    val = int(user)
    if(val):
        if val > 0:
            print(val,'is a Positive Number')
        elif val < 0:
            print(val,'is a Negative Number')
        else:
            print('Zero')

