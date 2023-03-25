tuple1 = (50,10,60,70,50)

count = 0
value = 50
for val in tuple1:
    if val == value:
        count+=1
print(f'{value} is available: ',count,'times')

#you can use alternative option:
#you can use count function to count:

tuple2 = (50,10,60,70,50)
value1 = 50
count_val = tuple2.count(value1)
print(count_val)
