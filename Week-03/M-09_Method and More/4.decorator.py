# Method-01:Decoration:

# def timer(func):
#     def inner():
#         print('Time Start')
#         func()
#         print('Time End')
#     return inner

# def get_factorial():
#     print('factorial')

# timer(get_factorial)()

# Method-02:Decoration:

# def timer(func):
#     def inner():
#         print('Time Start')
#         func()
#         print('Time End')
#     return inner

# @timer
# def get_factorial():
#     print('factorial')

# get_factorial()

# Method-03:
import math
import time
def timer(func):
    def inner(*args,**Kargs):
        print('Time Start')
        start = time.time()
        func(*args,**Kargs)
        end = time.time()
        print(f'Time End.Total time taken {end-start}')
    return inner
@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

# get_factorial(8)

# get_factorial(n=5)
get_factorial(n=120)

