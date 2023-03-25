#Python Exception Handling
#Syntax error vs exception

# def add(x) #syntex error
#     x /= 3


# def add(x):
#     x /= 0  #ZeroDivisionError: division by zero
#     print(x)
# add(5)

#For Exception Handling,There are four keyword:
"""
1.try
2.except
3.else
4.finally
"""
#try:
try:
    x = 10/2
    print(x)

except:
    print("Exception found")

# except ZeroDivisionError:
#     print("Zero Division Error found")

# except ValueError:
#     print("Value Error found")

else:
    print("No error found")

finally:
    print("I will be always printed")



