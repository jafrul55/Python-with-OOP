def Voter(age):
    if age < 18:
        raise ValueError("Voter is not in right age")
    return "You can vote here"

try:
    print(Voter(17))

except ValueError:
    print("Your age is "+str(18 - age)+ "less")



