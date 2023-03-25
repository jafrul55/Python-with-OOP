#namespace,scope

#Namespace defination:
""" 
A namespace is a collection of currently 
defined symbolic names 
along with information about
the object that each name references.
"""

"""
What is namespace type in Python?
In Python, there are four types of namespaces which are given below. 
1.Built-in, 
2.Global, 
3.Enclosing, 
4.Local.
"""

# keyword: local module,built_in_module
# x = 4
# x = 5
# y = 10

# def f():
#     x = 10 #Local scope
#     print("")


# import numpy as np
# np.f()
# LEGB
# L = Local
# E = Enclosed(nested function)
# G = Global
# B = Builtin

#local scope and global scope
# s = "I am global"

# def f():
#     s = "I am local"
#     print(s)
# f()
# print(s)

# Enclosed scope:
# s = "I am Global"
# def outer_scope():
#     s = 'I am Local'
#     def inner_scope():
#         # s = "I am enclosed"
#         print(s)
#     inner_scope()
# outer_scope()


#local,global,builtin,enclosed:
from math import pi #builtin scope
# print(pi)
# pi = 34.11 #global scope
# print(pi)
def outer_scope():
    # pi = 33.345 #outter scope
    # print(pi)
    def inner_scope():
        # print("I am enclosed")
        # pi = 3.345 #enclosed scope
        print(pi)
    inner_scope()
outer_scope()
# print(pi)

# enclosed > local > global > builtin

