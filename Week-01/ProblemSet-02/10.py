N = int(input("Enter Your Number: "))

for i in range(N):
    for j in range(i):
        print("* ",end="")
    print()

for i in range(N,0,-1):
    for j in range(i):
        print("* ",end="")
    print()