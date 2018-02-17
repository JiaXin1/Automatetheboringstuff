#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 07:51:54 2018

@author: CLin
"""

'''
Map, Filter, Reduce
'''

#==============================================================================
# #Blueprint - Map
#==============================================================================
#map(function_to_apply, list_of_inputs)

items = [1,2,3,4,5]
squared = [] #empty list
for i in items:
    squared.append(i**2)
    
#items = [1,2,3,4,5]
#squared = list(map(lambda x: x**2, items))
#print(squared) 

#output: [1, 4, 9, 16, 5]
    
    
def multiply(x):
    return(x*x)
def add(x):
    return(x+x)

funcs =[multiply, add]
#for i in range(5):
#    value = list(map(lambda x: x(i), funcs))
#    print(value)

#Filter 
#filter(function or None, iterable)
#number_list = range(-5,5)
#less_than_zero = list(filter(lambda x: x<0, number_list))
#print(less_than_zero)

#output: [-5, -4, -3, -2, -1]

#Reduce - applies a rolling computation to a sequential pairs of values
#in a list. 
'''
compute the product of a list of integers
'''

product = 1
alist = [1,2,3,4]
for num in alist:
    product = product * num

#reduce((function, sequence[,initials]))
from functools import reduce
product = reduce((lambda x, y: x*y),[1,2,3,4])


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

'''
Filter - return a new list that contains only those elements are 'True'
x%3==0 computes the remainder of x divided by 3
'''
print (filter(lambda x: x%3 == 0, foo))
# output: [18, 9, 24, 12, 27]

'''Map - convert the list
''' 
print (map(lambda x: x*2 +10, foo))
#output: [14, 46, 28, 54, 44, 58, 26, 34, 64]

''''Reudct - worker function' must accept 2 arguments (x and y)
'''
print (reduce(lambda x,y: x+y, foo))
#output: 139








