import csv
with open('./data/my_friends.csv','r') as file:
    lines = csv.reader(file)
    #if we use it then header will vanish
    header = next(lines) 
    for line in lines:
        print(line)
    print(header)