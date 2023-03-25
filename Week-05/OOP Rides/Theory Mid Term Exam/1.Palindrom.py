def Palindrom(S):
    reverse = S[::-1]
    if reverse == S:
        return "Palindrome"
    else:
        return "Not palindrome"


S = input("Enter Your input:")
val = Palindrom(S)
print(val)

