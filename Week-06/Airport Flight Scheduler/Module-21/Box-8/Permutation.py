""" 
A B C

A B C
A C B
B A C
B C A
C A B
C B A

"""

"""
DAC DUB LON IST PAR NYC KAT

"""
#python built in function: itertools
from itertools import permutations
# list = [1,2,3,4]
list = ['I','learn','Python']
for i in permutations(list):
    print(i)