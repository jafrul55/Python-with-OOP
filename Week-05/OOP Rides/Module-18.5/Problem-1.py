S = input()
a,b,c,d = map(int,input().split())

slice1 = S[a:b+1]
slice2 = S[c:d+1]

result = f"{slice1} {slice2}"
print(result)