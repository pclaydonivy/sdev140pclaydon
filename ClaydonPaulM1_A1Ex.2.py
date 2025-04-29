"""
Program: Meal Receipt
Name: Paul Claydon
DLM: 1/24/2025
purpose: takes the total cost of food items at a resteraunt, takes user input for % of 
    item cost to tip, and adds 7% of item cost as sales tax
"""

# Call in math module so i can use math.ceil to round up instead of rounding normally
import math

# declaring variables
itemCost = float(input("Please enter the total of the items in the order: $"))
tipPercent = int(input("Please enter the percent you would like to tip: "))
customTip = float((itemCost / 100) * int(tipPercent))
salesTax = float((itemCost / 100) * 7)
orderTotal = itemCost + customTip + salesTax

# this part is a wee bit dumb
# Convert from $ and cents to just cents
itemCost = itemCost * 100
customTip = customTip * 100
salesTax = salesTax * 100
orderTotal = orderTotal * 100

# Round up
itemCost = math.ceil(itemCost)
customTip = math.ceil(customTip)
salesTax = math.ceil(salesTax)
orderTotal = math.ceil(orderTotal)

# Convert back to $ and cents
itemCost = itemCost / 100
customTip = customTip / 100
salesTax = salesTax / 100
orderTotal = orderTotal / 100

# with round(), you can use a second argument to set what decimal place it rounds to,
# redering over half the code used here pointless. 
# ex: round(87.153, 1) will result in 8.2
# math.ceil & math.floor do not have this feature. I am very hesitant to forgive this.

# Display item cost, Amount tipped, Tax, & Total
print("items: $", itemCost) 
print("  tip: $", customTip)
print("  Tax: $", salesTax )
print("Total: $", orderTotal)
