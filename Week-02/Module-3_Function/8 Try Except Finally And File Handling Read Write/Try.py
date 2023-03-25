# num = 15/0
# print(num)

#if you want to ignore error:
try:
    # num = 15/0
    num = 15/5
    print(num)

except:
    print('Someting went wrong')
finally:
    print('This is done')