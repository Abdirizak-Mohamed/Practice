#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:08:27 2019

@author: amohamed5
"""

annual_salary = float(input("How much you make" )) 
portion_saved =float(input("How much will you save each month" ))
total_cost = int(input("How much is total Cost" ))

current_savings = 0 
number_months = 0 

while current_savings < total_cost:
    ((current_savings * 0.04) / 12) + (annual_salary * (portion_saved / 100))
    number_months + 1 

print(number_months)