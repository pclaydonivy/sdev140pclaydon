"""
Program: Celcius to Fahrenheit
Name: Paul Claydon
DLM: 1/24/2025
purpose: Takes user input of a floating point integer as a temperature in Celcius,
   then converts it into Fahrenheit for the user.
"""

Celcius = float(input("Please enter the temperature in celcius that you want to convert:"))
Fahrenheight = Celcius * 1.8 + 32
print(Celcius, "degrees Celcius is equivelant to", Fahrenheight, "degrees Fahrenheit")