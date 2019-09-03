#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:17:52 2019

@author: amohamed5
"""

annual_salary = 150000 
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * 0.25
number_of_months = 0
portion_saved = 3750
current_savings = 0
number_its = 0 
bi_annual = 0 

5000
2500
1250
625
313
469




for number_months in range(0, 37) :
    interest = ((current_savings * 0.04)/12)
    savings = (annual_salary / 12) * (portion_saved/10000)
    print(interest)
    print(savings)
    current_savings = current_savings + interest + savings 
    annual = bi_annual / 6
    
    if annual % 1 == 0 and annual != 0: 
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

        
    bi_annual = bi_annual + (1)
    number_months = number_months + 1
    print(current_savings)

print(number_its)
print(current_savings)  
290754
431801