#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 06:48:04 2019

@author: amohamed5
"""
print("How much you make  each   ")
annual_salary = float(input()) 
print("How much will you save each month   " )
portion_saved = float(input())
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
    portion_saved = (high + low) / 2
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
   
while current_savings < 249900 and current_savings > 250100  : 
     if current_savings > 250100:
         current_savings = 0 
         interest = 0 
         savings = 0 
         number_months = 0 
         bi_annual = 0 
         portion_saved = 0 
         low = portion_saved
         number_its += 1
         break
 
     elif current_savings > 250100:
         current_savings = 0 
         interest = 0 
         savings = 0 
         number_months = 0 
         bi_annual = 0 
         portion_saved = 0 
         high = portion_saved
         number_its += 1
         break
         
     
        while current_savings > 251000 and current_savings < 249900:
    if current_savings > 251000: 
        high = portion_saved
        number_its += 1 
    elif current_savings < 249900 :
        low = portion_saved
        number_its += 1 
    
    portion_saved = (high + low) / 2
    bi_annual = 0 
    current_savings = 0
    interest = 0 
    savings = 0

        
print("Number of Months:", number_its)