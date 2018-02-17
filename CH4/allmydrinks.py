#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:23:23 2018

@author: CLin
"""

drinks = []
while True:
    print('Enter the name of the drink' + str(len(drinks)+1) +'(Or enter nothing to stop.)')
    new_drink= input()
    if new_drink == '':
        break
    drinks = drinks + [new_drink] #list concatenation 
    print('The availible drinks are:')
    for name in drinks:
        print(''+name)
