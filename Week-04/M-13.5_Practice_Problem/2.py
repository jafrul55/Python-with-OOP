# call function with decorator:
# def uppercase_decorator(function):
#     def wrapper(*args,**kargs):
#         result = function(*args,**kargs)
#         return result.upper()
#     return wrapper

# @uppercase_decorator
# def greet(name):
#     return "Hello, " + name

# print(greet('Jafrul'))

#function call without decorator:
def greet(name):
    return "Hello, " + name
print(greet("Jafrul"))