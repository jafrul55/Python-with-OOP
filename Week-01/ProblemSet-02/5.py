S1 = input("String1: ")
S2 = input("String2: ")
S3 = ""
while S1 and S2:
    S3 += S1[0] + S2[-1]
    S1 = S1[1:]
    S2 = S2[:-1]

print(S3)