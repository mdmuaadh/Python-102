# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: ENGR 102 - 559
# Assignment: Lab 3-Activity 2 
# Date: 09/08/2025

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# 

side= float(input("Please enter the side length:"))

#Area of equilateral triangle 
area_triangle = (sqrt(3)/4) * (side**2)
printresult("triangle", side, area_triangle)

#Area of Square
area_square = side**2
printresult("square", side, area_square)

#Area of Regular Pentagon
area_pentagon= (1/4) * sqrt(5*(5+2*sqrt(5)))* (side **2)
printresult("pentagon", side, area_pentagon)

#Area of Regular Hexagon
area_hexagon = (3*sqrt(3)/2) * (side**2)
printresult("hexagon", side, area_hexagon)

#Area of a regular dodecagon (12 sides)
area_dodecagon= 3*(2+sqrt(3)) * (side**2)
printresult("dodecagon",side, area_dodecagon)

