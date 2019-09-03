#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:01:47 2019

@author: amohamed5
"""

high = 1000
low = 0 


ps = (high + low) / 2
john = 1000 / ps 
number_its = 0 

while john != 10:
    
    if john > 10 :
       low = ps  
    elif john < 10 :
       high = ps 
    
    number_its += 1 
    ps = int((high + low) / 2)
    john = 1000 / ps
       
print(number_its)
       