# Example 1: Creating 1d list Using Naive methods
N = 5
ar = [0]*N
# print(ar)

#Creating a 1d list using  List Comprehension
N = 5
ar = [0 for i in range(N)]
# print(ar)

#Method 2 Creating a 2-D list
rows,cols = (5,5)
ar = [[0]*cols]*rows
# print(ar)

#To update row and column:
row,col = (5,5)
arr = [[0]*col]*row
# print(arr,'Before')

arr[0][0] = 1 #update only one element
# print(arr,"after")

#Using List comprehension:
row,col = (5,5)
arr = [[0 for i in range(col)] for j in range(row)]
# print(arr)

arr[1][3] = 13
arr[2][3] = 23
# print(arr)

# Using empty list
arr = []
rows,cols = 5,5
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
# print(arr)
#----------------------------
#method 2 1st approach:
# rows,cols = (5,5)
# arr = [[0]*cols]*rows

# arr[0][0] = 121

# for row in arr:
#     print(row)

#output Will be:
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]

#Method 2 2nd approach:
cols,rows = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 1
arr[3][3] = 33
for row in arr:
    print(row)

#output:
# [1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]




