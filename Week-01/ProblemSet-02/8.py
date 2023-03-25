L = int(input('Start: '))
R = int(input('End: '))
for i in range(L,R+1):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)