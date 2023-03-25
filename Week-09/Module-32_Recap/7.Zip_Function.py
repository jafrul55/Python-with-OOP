#zip:
"""
The zip function is a built-in Python function
that takes two or more iterables (such as lists, tuples, or strings) 
and returns an iterator that aggregates them into tuples. 
Each tuple contains one element from each of the input iterables, 
in the order they were passed to the zip function. 
"""
# Example -1:

# nums = [1,2,3]
# string = ["one","two","three"]
# num = [1.1,2.2,3.3] #float
#But if I take more value which has no pair then it never take
# num = [1.1,2.2,3.3,4.4]
# new_object = zip(nums,string,num)
# print(tuple(new_object))
# print(set(new_object)) #no index and unorder
# print(list(new_object))

# Example -2:
#if we try to take as a set:
# nums = {1,2,3}
# string = ["one","two","three"]
# num = [1.1,2.2,3.3] #float
# new_object = zip(nums,string,num)
# print(list(new_object))

#Example -3:
# names = ["rahim","karim","halim"]
# salaries = [10000,20000,15000]
# print(list(zip(names,salaries)))

# new_db = {name:salary for name,salary in zip(names,salaries)}
# print(new_db)
# print(new_db['rahim'])

#Example -4: Zip to Unzip:
names = ["rahim","karim","halim"]
salaries = [10000,20000,30000]
result = list(zip(names,salaries))
# print(result)

#it will split result and unzip result
name,salary = zip(*result)
print(name)
print(salary)




