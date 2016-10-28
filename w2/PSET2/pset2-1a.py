"""
The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      
monthlyInterestRate = annualInterestRate/12.0

for month in range(12):
    p_min = balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - p_min
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print(round(balance,2))