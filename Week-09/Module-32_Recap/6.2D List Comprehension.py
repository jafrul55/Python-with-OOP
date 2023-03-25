#List Comprehension:
# lst = [[j for j in range(3)] for i in range(4)]
# print(lst)

#it is dengerous topic: we never use it:
# r,c = (5,5)
# lst = [[0]*c]*r
# print(lst)
# lst[0][0] = 1
# print(lst)

#Both address will be same
# print(id(lst[0]))
# print(id(lst[1])) 

# But we want different address:
# lst = [[0 for j in range(5)] for i in range(5)]
#we also change row and col wise value change:
# lst[0][1] = 1
# print(lst)
#Both address will be different:
# print(id(lst[0]))
# print(id(lst[1]))
# print(lst)

#2D list Convert in 1D list(Sublist):Fluten
# Example -1:
# lst = [[1,2,3],[4,5],[6,7,8]]
# new_lst = [sublist for val in lst for sublist in val]
# print(new_lst)

# Example -2: if word len > 5
lst = [["hello","world"],["mango","banana"],["python","java"]]
new_lst = [sublist for val in lst for sublist in val if len(sublist) > 5]
print(new_lst)
