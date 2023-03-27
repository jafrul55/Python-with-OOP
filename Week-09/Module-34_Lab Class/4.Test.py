import pandas as pd
import math
import json
import matplotlib.pyplot as plt

data = pd.read_csv("salary.csv")
headers = data.columns.values
X = data[headers[0]]
Y = data[headers[1]]
X = X.truncate(4900,4999)
Y = Y.truncate(4900,4999)

#read from train_data.txt
with open("train_data.txt") as file:
    data = file.read()
    converted = json.loads(data)
    # print(converted)
    # print(converted["m"])
    # print(converted["c"])
#Formula for Test:
#Y = mx + c
m = converted["m"]
c = converted["c"]
Y_mean = converted["Y_mean"]
Y_predict_list = []
r_upper = 0
r_lower = 0

for index in range(len(X)):
    Y_predict = (m*X[index+4900])+c
    Y_predict_list.append(Y_predict)
    r_upper += math.pow((Y[index+4900]- Y_predict),2)
    r_lower += math.pow((Y[index+4900]-Y_mean),2)

r_square = 1 - (r_upper/r_lower)
print(r_square)

inp = int(input("Enter year of experiance: "))
predicted = (m*inp) + c
print(f"predicted salary: {predicted}")

# for val in X:
#     Y_predict = (m*val) + c
#     Y_predict_list.append(Y_predict)

# plt.scatter(X,Y,color = "g")
# plt.plot(X,Y_predict_list,color='r')
# plt.show()

