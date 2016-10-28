# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 00:06:17 2016

@author: apple
"""

balance = 3329
annualInterestRate = 0.2
	      
monthlyInterestRate = annualInterestRate/12.0
p = 0
copybalance = balance

while balance > 0:
    balance = copybalance
    p += 10
    for month in range(12):
        monthlyUnpaidBalance = balance - p
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print("Lowest Payment: " + str(p))