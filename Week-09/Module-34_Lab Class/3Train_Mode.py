import pandas as pd
import math
import json

data = pd.read_csv("salary.csv")

# Function to calculate mean
def calculate_mean(data):
    sum = 0
    for val in data:
        sum += val
    mean = sum/len(data)
    return mean

# Extracting x and y columns from dataset
headers = data.columns.values
x = data[headers[0]]
y = data[headers[1]]

x=x.truncate(0,4899)
y=y.truncate(0,4899)

# Calculate mean for x and y
x_mean = calculate_mean(x)
y_mean = calculate_mean(y)

# Perform linear regression to find slope and intercept
upper = 0
lower = 0
for index in range(len(x)):
    upper += (x[index] - x_mean) * (y[index] - y_mean)
    lower += math.pow(x[index] - x_mean,2)
m = upper/lower
c = y_mean - (m*x_mean)

# print(m,c)

# Save calculated slope and intercept in a dictionary and write it to a file
Train_data = {}
Train_data["m"] = m
Train_data["c"] = c
Train_data["Y_mean"] = y_mean

with open("train_data.txt",'w') as file:
    file.write(json.dumps(Train_data))
