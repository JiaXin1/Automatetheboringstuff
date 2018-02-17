#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:09:52 2018

@author: CLin
"""

'''PASSING REFERENCE'''

def peeps(someParameter):
    someParameter.append('Claire')
    
employee = ['Jack','Sarah','Wendy']
peeps(employee)
print(peeps)

#Even though employee and someParameter contain separate references, 
#they both refer to the same list. This is why the append('Hello') method 
#call inside the function affects the list even after the function call 
#has returned.

#Keep this behavior in mind: Forgetting that Python handles list and 
#dictionary variables this way can lead to confusing bugs.