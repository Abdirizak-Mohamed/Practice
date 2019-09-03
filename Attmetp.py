#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:26:29 2019

@author: amohamed5
"""

print("How much you make  each   ")
annual_salary = float(input()) 
print("How much will you save each month   " )
portion_saved = 0
print("How much is total Cost    ")
total_cost = float(input())
print("Raise?")
semi_annual_raise = float(input())

portion_down_payment = total_cost * 0.25


current_savings = 0
number_months = 0
bi_annual = 0
high = 10000
low = 0 
number_its = 0 


while current_savings < portion_down_payment:
    portion_saved = int((high + low) / 2)
    interest = ((current_savings * 0.04)/12)
    savings = (annual_salary / 12) * (portion_saved/100)
    current_savings = current_savings + interest + savings 
    annual = bi_annual / 6
    
    if annual % 1 == 0 and annual != 0: 
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

        
    bi_annual = bi_annual + (1)
    number_months = number_months + 1
    if number_months >= 37:
        break
   
while number_months != 36 : 
     if number_months > 36:
         current_savings = 0 
         interest = 0 
         savings = 0 
         number_months = 0 
         bi_annual = 0 
         portion_saved = 0 
         low = portion_saved
         number_its += 1
         portion_saved = int((high + low) / 2)
         break
 
     elif number_months > 36:
         current_savings = 0 
         interest = 0 
         savings = 0 
         number_months = 0 
         bi_annual = 0 
         portion_saved = 0 
         high = portion_saved
         number_its += 1
         portion_saved = int((high + low) / 2)
         break
    
print(number_its) 