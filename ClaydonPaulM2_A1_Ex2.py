"""
Program: Factorial Calculator
Author: Paul Claydon
DLM: 2/10/2025
Purpose: 
Variables: integer, factorialProduct, count
"""

# Explain program purpose to user
print("This program Calculates the factorial of a nonnegative integer n.")
print("In mathematics, the notation n! represents the factorial of the nonnegative integer n.")
print("The factorial of n is the product of all the nonnegative integers from 1 to n. For example,\n7!=1*2*3*4*5*6*7=5,040\n4!=1*2*3*4=24")
print("")
# take (Factorial Number) = int(input()) > 0
integer = int(input("put positive integer here: "))
factorialProduct = 1
count = 1
if integer <= 0 :
    factorialProduct = "Error: Factorial must be a positive integer for program to run."
    # this is here to give an error message when the integer input is not a positive number. 
    # the entire while loop gets skipped because it only triggers if var count is less than var integer.
    # var count is always = to 1 at this point in the program, so if var integer is less than 1, it does nothing.
    # Thus using the same math logic to decide between outputing an answer or an error message is a an option i can use here
while count <= integer : 
    factorialProduct = factorialProduct * count
    count += 1
# Decision to give error message or output results
if integer <= 0 :
    print(factorialProduct)
else :
    print("If", integer, "= n!, \nThe factorial of n! is ", factorialProduct)
