"""
Program: tidbit.py
Author: Paul Claydon
DLM: 2/6/25
Purpose: 
Input  
    purchase_price
Constants
    annual interest rate = 12%
    d payment = 10%
    monthly payment = 5% of purchase_price
"""
ANNUAL_RATE = .12
MONTHLY_RATE = ANNUAL_RATE / 12

purchasePrice = float(input("Enter in the purchase price: "))

downPayment = purchasePrice * 0.1
purchasePrice = purchasePrice - downPayment

monthlyPayment = purchasePrice * 0.05
month = 1
balance = purchasePrice
print("Month  starting balance  interest to pay  principal to pay  payment  ending balance")
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else: 
        interest = balance * MONTHLY_RATE
    principal = monthlyPayment - interest
    remaining = balance - principal
    print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % (month, balance, interest, principal, monthlyPayment, remaining))
    balance = remaining
    month += 1

    """
    Figure out a way to print an additional variable at the end"""