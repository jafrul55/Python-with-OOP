def exp(a,n):
    return a**n

a,b = map(int,input('enter numbers: ',).split())
val = exp(a,b)
print('result is: ',val)
