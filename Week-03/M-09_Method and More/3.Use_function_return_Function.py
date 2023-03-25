# 3 Use function as parameter and return function
# def do_somthing(x,y):
#     print(f'x: {x} y: {y}')

# do_somthing(12,45)
# do_somthing('tomato','onion')

# Function inside of Function parameter call:
def do_somthing(work):
    print('Start the work')
    print(work)
    print('Done with the work')

do_somthing(23)

print('\n')

def do_somthing(work):
    print('Start the work')
    work()
    print('Done with the work')

def practice_coding():
    print('I am practicing python')

do_somthing(practice_coding)

print('\n')

def do_somthing(work):
    print('Start the work')
    work()
    print('Done with the work')

def practice_coding():
    print('I am practicing python')
    
def learning_python():
    print('learning python class')

do_somthing(practice_coding)
do_somthing(learning_python)