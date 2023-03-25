# def func(arg1,arg2,arg3=4,arg4=5):
#     print(arg1,arg2,arg3,arg4)

# func(6,7)


# def func(arg1,arg2,arg3=4,arg4=5):
#     print(arg1,arg2,arg3,arg4)

# func(4,5,arg3=6)


# def func(arg1,arg2,arg3=4,arg4=5):
#     print(arg1,arg2,arg3,arg4)

# func() 
# output:TypeError/TypeError: func() missing 2 required positional arguments: 'arg1' and 'arg2'

def func(arg1,arg2,arg3=4,arg4=5):
    print(arg1,arg2,arg3,arg4)

func(3,4,arg2=1)