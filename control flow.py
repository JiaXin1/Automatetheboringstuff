#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:15:13 2018

@author: CLin
"""

name = 'Mary'
password = 'swordfish'
if name =='Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Wrong password.')
        

name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kid')
elif age > 100:  #true 
    print('You are not Alice, grannie')
elif age > 2000: #true - but not executed 
    print('You are not Dracula')
    

name = 'Alice'
age = 25
if name == 'Claire':
    print('Hi Claire')
elif age < 10:
    print('You are not Alice, kid')
elif age == 64: 
    print('You are not Alice, grannie')
else: #will be executed 
    age == 25
    print('Hi Alice')
    

product = 1
alist = [1,2,3,4]
for num in alist:
    product = product * num