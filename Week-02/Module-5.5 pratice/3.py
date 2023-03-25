# def add_list(list1,list2):
#     new_list = []
#     for i in range(max(len(list1),len(list2))):
#         if i < len(list1) and i < len(list2):
#             new_list.append(list1[i] + list2[i])
#         elif i < len(list1):
#             new_list.append(list1[i])
#         else:
#             new_list.append(list2[i])
#     return new_list
# list1 = ["M","na","i","Bo"]
# list2 = ["y","me","s","nd"]
# print(add_list(list1,list2))


# you can do it without function call
# list1 = ["M","na","i","Bo"]
# list2 = ["y","me","s","nd"]
# result = []
# for i in range(max(len(list1),len(list2))):
#     if i<len(list1) and i < len(list2):
#         result.append(list1[i] + list2[i])
#     elif i < len(list1):
#         result.append(list1[i])
#     else:
#         result.append(list2[i])
# print(result)

# You can also use zip function to solve this question:

list1 = ["M","na","i","Bo"]
list2 = ["y","me","s","nd"]

result = [val1 + val2 for val1,val2 in zip(list1,list2)]
print(result)