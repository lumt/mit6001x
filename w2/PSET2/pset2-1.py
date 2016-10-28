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
p = 10
copybalance = balance

while balance > 0:
	balance = copybalance

	for month in range(12):
	    monthlyUnpaidBalance = balance - p
	    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

	p += 10


print(round(balance,2))
print(p)