#Sequencial Data Type Slicing (string,list,tuple):
#list:
lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst[-1])
# print(lst[-3])
# print(lst[0:3])  #start : end = end - start
# print(lst[:])
# print(lst[-1:-4]) #it's not work
# print(lst[-4:-1]) #it's will work
# lst[0:3] = [0,0,0]
# print(lst)
# print(lst[0:10:2]) #start : end : step
# print(lst[::-1]) #to make reverse

#string:
s = "I love python"
# s[0:3] = "hello" #'str' object does not support item assignment 
# print(s[0:4:2])
# print(s[::-1]) #to make string reverse

#Tuple:
t = (1,2,3,4,5,6,7,8,9,10)
# print(t[0:3])
#We have also slice funtion:
# slice(start,end,step):
new_lst = slice(0,3) #formal way te slice kore
# print(new_lst)
print(lst[new_lst])


