def do_somthing():
    print('Inside the function do_somthing')
    def inner_function():
        print('Inside the inner function')
    inner_function()

# do_somthing()

def first_function():
    print('inside the first funtion')
    def second_function():
        print('inside the inner function')
    return second_function

first = first_function()
first()
#you can call two function one by one
# first_function()()