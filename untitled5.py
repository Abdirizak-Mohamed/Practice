#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:37:29 2019

@author: amohamed5
"""

annual_salary1 = float(input())
annual_salary = annual_salary1 

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * 0.25
number_of_months = 0
low = 0 
high = 10000
current_savings = 0
number_its = 0 
bi_annual = 0 
portion_saved = int(((high + low) / 2)) 
number_months = 0 


for number_months in range(0, 37) :
    interest = ((current_savings * 0.04)/12)
    savings = (annual_salary / 12) * (portion_saved/10000)
    current_savings = current_savings + interest + savings 
    annual = bi_annual / 6
    
    if annual % 1 == 0 and annual != 0: 
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

        
    bi_annual = bi_annual + (1)
    number_months = number_months + 1  




print(current_savings)
print(portion_saved)

while current_savings < 249900 or current_savings > 250100  : 
     if current_savings > 250100:
         print(current_savings)
         current_savings = 0 
         interest = 0 
         savings = 0 
         number_months = 0 
         bi_annual = 0 
         annual = 0
         annual_salary = annual_salary1
         high = portion_saved
         print(high, low)
         number_its += 1
         portion_saved = (int(high) + int(low)) / 2
         print("high", current_savings)
         print("Portion Saved:", portion_saved)
         
         
 
     elif current_savings < 249900:
         print(current_savings)
         current_savings = 0 
         interest = 0 
         savings = 0 
         number_months = 0 
         bi_annual = 0 
         annual = 0 
         annual_salary = annual_salary1
         low = portion_saved
         print(high, low)
         number_its += 1
         portion_saved = (int(high) + int(low)) / 2
         print("LOW", current_savings)
         print("Portion Saved:", portion_saved)
         
   
            
     for number_months in range(0, 37) :
         interest = ((current_savings * 0.04)/12)
         savings = (annual_salary / 12) * (portion_saved/10000)
         current_savings = current_savings + interest + savings 
         annual = bi_annual / 6
    
         if annual % 1 == 0 and annual != 0: 
             annual_salary = annual_salary + (annual_salary * semi_annual_raise)

        
         bi_annual = bi_annual + (1)
         number_months = number_months + 1  
         
     if portion_saved == 9999.5: 
         print("this Ain't working boo")
         break
    
print(current_savings)
print(number_its)
print(portion_saved / 100)


