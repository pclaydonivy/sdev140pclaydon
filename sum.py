"""
Program: Average Calculator
Name: Paul Claydon
DC: 1/30/2025 DLM:
Purpose: A program in a file named sum.py that recieves a series of numbers from the user, 
generates an average of the given inputs upon recieving a blank input, then outputs the average with print

"""

# Initialize variables
# Initialize the cont of numbers
count = 0
# Initialize the sum of numbers
theSum = 0.0
# Initialize the avg of numbers
theAvg = 0.0
# Get the first number from user
print("This program takes number inputs from the user to generate an average.")
data = input("enter a number or press enter to quit: ")
# Loop to get the rest of the numbers
while data !="":
    #
    number = float(data)
    # Add the next number to theSum
    theSum +=  number
    # Increment the count
    count += 1
    # Get the next number from the user
    data = input("enter a number or press enter to quit: ") 
# Calculate the average
theAvg = theSum / count
# Output theSum & theAvg
print("User has pressed Enter to quit.")
print("The average of the input numbers is : ", theAvg)

"""
Pseudocode from assignment page below


Initialize theSum to 0
Initialize count to 0

while True:
    Display "Enter a number or press Enter to quit: "
    Read input into number
    
    if number is an empty string
        Break out of the loop
    
    Convert number to a floating-point value and add it to theSum
    Increment count by 1

Display "The sum is", theSum
if count is greater than 0
    Display "The average is", theSum divided by count
"""