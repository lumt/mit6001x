# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:16:56 2016

@author: apple
"""

balance = 999999
annualInterestRate = 0.18

copybalance = balance
monthlyInterestRate = annualInterestRate/12.0
lower = balance / 12
upper = (balance*(1+monthlyInterestRate)**12)/12

while abs(balance) > 0.01:
    balance = copybalance
    p = (lower + upper)/2
    
    for month in range(12):
        monthlyUnpaidBalance = balance - p
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        
    if balance > 0:
        lower = p
    elif balance < 0:
        upper = p
    
print("Balance remaining: " + str(balance))
print("Lowest Payment: " + str(round(p,2)))