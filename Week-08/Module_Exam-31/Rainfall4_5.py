from math import sqrt


rainfall_data = []
for i in range(7):
    data = float(input("Enter data for week {}: ".format(i+1)))
    rainfall_data.append(data)

#Calculate the mean of the rainfall data:
mean = sum(rainfall_data)/len(rainfall_data)

#Calculate the standard deviation of the rainfall_data
deviation_sum = 0
for data in rainfall_data:
    deviation_sum += (data-mean) **2

# print(deviation_sum) #28.0
variance = deviation_sum/len(rainfall_data)
# standard_deviation = sqrt(variance)
standard_deviation = variance ** 0.5

#find the day with minimum rainfall
MIN_data = min(rainfall_data)
min_rainfall_day = rainfall_data.index(MIN_data) + 1

#find the day with maximum rainfall
MAX_data = max(rainfall_data)
max_rainfall_day = rainfall_data.index(MAX_data) + 1


print("This is the day {} with Minimum Rainfall {:.2f} mm".format(min_rainfall_day,MIN_data))
print("This is the day {} with Minimum Rainfall {:.2f} mm".format(max_rainfall_day,MAX_data))
print("The mean of the rainfall data is {:.2f} mm".format(mean))
print("The standard deviation of the rainfall data is {:.2f} mm".format(standard_deviation))


""" Standard Deviation Formula:
variance = (1/n) * sum((xi - mean)^2)

Where:

n is the number of data points
xi is the ith data point
mean is the mean of the data

standard deviation = sqrt(variance)



"""