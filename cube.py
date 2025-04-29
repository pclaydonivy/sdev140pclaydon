"""
Program: Cube Surface Area Calculator
Name: Paul Claydon
DLM: 1/27/2025
Purpose: To take a cube's edge length as an input, and use it to find the surface area of the cube.
    The conversion is done by taking the input to the power of 2, and then multiply by the number of sides (6)
    The answer will be the resulting number^2. It should be printed as answer^2 (ex: 24^2, 150^2)
    (I would make the print() commands display as such, but i dont know how to do that :/)
"""

print(""" This program uses the edge length of a cube to find the surface area of said cube
    Parameters:
    edgeLength (int): The input value that is the length of a cube's edge length

    Output:
    surfArea (int): The Surface Area of the cube in question. result of '(edgeLength)^2 * 6'
      
    input edgeLength
    surfArea = (edgeLength * edgeLength) * 6
    output surfArea
    """)
edgeLength = int(input("please enter the length of the edge: "))
surfArea = (edgeLength ** 2) * 6
print("A cube with an edge length of", edgeLength, "units")
print("will have a surface area of", (surfArea), "^2 square units")