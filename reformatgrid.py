#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:06:56 2018

@author: CLin
"""

grid = [['.', '.', '.', '.', '.', '.'],  #1
        ['.', 'O', 'O', '.', '.', '.'],  #2
        ['O', 'O', 'O', 'O', '.', '.'],  #3
        ['O', 'O', 'O', 'O', 'O', '.'],  #4
        ['.', 'O', 'O', 'O', 'O', 'O'],  #5
        ['O', 'O', 'O', 'O', 'O', '.'],  #6
        ['O', 'O', 'O', 'O', '.', '.'],  #7
        ['.', 'O', 'O', '.', '.', '.'],  #8
        ['.', '.', '.', '.', '.', '.']]  #9

#grid = 6x9
#print(len(grid)) #9 - Y
#print(len(grid[0])) #6 -X

def reformat(grid):
    for x in range(len(grid[0])):
        print()
        for y in range (len(grid)):
            print(grid[y][x], end='')

reformat(grid)