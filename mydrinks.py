#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:51:30 2018

@author: CLin
"""

drinks = ['latte','hot chocolate', 'milk','coke']
print('Enter a drink:')
name = input()
if name not in drinks:
    print('I do not have' + name+ 'on the menu.')
else:
    print(name + 'is not on the menu.')