balance = 580

# def total_cost(price,quantity):
#     cost = price * quantity
#     balance = 100
#     remaining = balance - cost
#     balance = remaining
#     print(remaining)
#     return cost

# pay = total_cost(10,3)
# print(f'please pay: {pay}')

# if you want to use global variable in function

def total_cost(price,quantity):
    global balance  #you have to use global keyword
    cost = price * quantity
    # balance = 100
    # remaining = balance - cost
    # balance = remaining
    balance = balance - cost
    # balance = cost
    # print(remaining)
    return cost

print(f'Balance Outside Before: {balance}')

pay = total_cost(10,3)
print(f'please pay: {pay}')
print(f'Balance outside After: {balance}')