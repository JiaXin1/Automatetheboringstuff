#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 05:56:35 2018

@author: CLin
"""

drinks = ['latte','hot chocolate', 'milk','coke']

'''
SUBLIST WITH SLICES'''

drinks[2] is a list with an index (one interger)
drinks[1:3] is a list with a slice (two intergers)

'''Len()'''
len(drinks)

'''Changing value in a list with indexes'''''
Drinks[3] = 'Iced Capp'

 '''LIST CONCATENATION AND REPLICATION'''
 [1,2,3]+['Apple'+'Banana'+'Choloate']
 
 ['Apple'+'Banana'+'Choloate']*3
 
Food = ['Apple'+'Banana'+'Choloate']
Food = Food +[1,2,3]

#REMOVE VALUES from list with Del statements
Coffee = ['latte','hot chocolate', 'milk','coke','Pepsi']
del Coffee[-1]


#USING FOR LOOP WITH LIST
drinks = ['latte','hot chocolate', 'milk','coke']
for i in range(len(drinks)):
    print('Index'+str(i)+'on the menu:' + drinks[i])

#IN AND NO IN OPERATOR
drinks = ['latte','hot chocolate', 'milk','coke']
'coke'in drinks #True
'pepsi' in drinks #False

#THE MULTIPLE ASSIGNMENT TRICK
Coffee= ['Medium', 'Double-Double', 'Hot','$1.05']
Size, Favour, Temperture, Price = Coffee

#AGUMENTED ASSIGNMENT STATEMENT
web = 'Hello'
web += 'World!'

web *= 3

'''METHOD'''
#find value - index()
coffee= ['Medium', 'Double-Double', 'Hot','$1.05']
coffee.index ('Medium')

coffee= ['Medium', 'Hot', 'Double-Double', 'Hot','$1.05'] #duplicate
coffee.index ('Hot')

#add value - append() and insert() ** list method
drinks = ['latte','hot chocolate', 'milk','coke']
drinks.append('water')

drinks = ['latte','hot chocolate', 'milk','coke','pepsi']
drinks.insert(0, 'iced capp')

#remove value - remove()
drinks = ['latte','hot chocolate', 'milk','coke','pepsi']
drinks.remove('pepsi')

#sort value - sort()
drinks = ['latte','hot chocolate', 'milk','coke','pepsi']
drinks.sort()
drinks

num = [123,23,17,24,5.3,88]
num.sort()
num

drinks = ['latte','hot chocolate', 'milk','coke','pepsi']
drinks.sort(reverse=True)
drinks

drinks = ['Latte','hot chocolate', 'milk','Coke','pepsi','apple juice']
drinks.sort(key=str.lower)
drinks


#new line 
print('Four score and seven ' + \
      'years ago...')


#list-like types: strings and tuples
drink = 'Coffee'
for i in drink:
    print('***'+i+'***')
    
#mutable and immutable data type
#string is immutable - can modify by slicing and concatenate

drink = 'coke is my favourite drink.'
newdrink = 'coffee' + drink[5:]
newdrink


'''TUPLE DATA TYPE'''

drink = ('coffe',) #trailing comma 
type(drink)

#converting 
tuple(['latte','hot chocolate', 'milk','coke','pepsi'])

list(('latte','hot chocolate', 'milk','coke','pepsi'))

list('coffe')
#Out['c', 'o', 'f', 'f', 'e']



'''COPY - copy() and deepcopy()'''
import copy 
drinks= ['latte','coffee','coke','milk']
new = copy.copy(drinks)
new[2]= 'iced capp'
drinks
new 



















