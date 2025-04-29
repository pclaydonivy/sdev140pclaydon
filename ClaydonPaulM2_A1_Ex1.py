"""
Program: Color Mixer
Author: Paul Claydon
DLM: 2/10/2025
Purpose: To take user input to choose two of the three primary colors to mix together, and then output the resulting color.
Variables: color1, color2, resultColor
"""

# Explaination for user
print("This program is designed to take two of the three primary colors (Red, Yellow, & Blue),")
print("mix them, and give the name of the resulting color.")
# Taking inputs in the form of strings
color1 = input("Enter the first primary color: ")
color2 = input("input the second primary color: ")
# Using loop to determine the resulting color based on input colors
if color1 == "yellow" and color2 == "yellow":
    resultColor = "yellow"
elif color1 == "yellow" and color2 == "red":
    resultColor = "orange"
elif color1 == "yellow" and color2 == "blue":
    resultColor = "green"
elif color1 == "blue" and color2 == "blue":
    resultColor = "blue"
elif color1 == "blue" and color2 == "yellow":
    resultColor = "green"
elif color1 == "blue" and color2 == "red":
    resultColor = "purple"
elif color1 == "red" and color2 == "red":
    resultColor = "red"
elif color1 == "red" and color2 == "blue":
    resultColor = "purple"
elif color1 == "red" and color2 == "yellow":
    resultColor = "orange"
# Error statement
else: print("Error: invalid input. Please only enter in primary colors (red, yellow, blue).")
# output results
print(color1, "and", color2, "combine into", resultColor)
