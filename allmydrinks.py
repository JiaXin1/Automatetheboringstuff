#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:23:23 2018

@author: CLin
"""

menu = []
while True:
    print('Enter the name of the drink' + str(len(menu)+1) +'(Or enter nothing to stop.)')
    new_menu= input()
    if new_menu== '':
        break
    drinks = menu + [new_menu] #list concatenation 
    print('The availible drinks are:')
    for name in menu:
        print(''+name)
        
       
