# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: ENGR 102 - 559
# Assignment: Lab 1 - Topic 3 
# Date: 08/30/2025

from math import cos
# The purpose of this assingment is to show how limits can be calculated numerically and help create computational python programs to introduce the basis of calculus through python
print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 0.75")
#printing out a sequence of eight numbers 
#Equation to follow 
x = 1.0; print((1 - cos(x)) / (x**2))
x = 0.1; print((1 - cos(x)) / (x**2))
x = 0.01; print((1 - cos(x)) / (x**2))
x = 0.001; print((1 - cos(x)) / (x**2))
x = 0.0001; print((1 - cos(x)) / (x**2))
x = 0.00001; print((1 - cos(x)) / (x**2))
x = 0.000001; print((1 - cos(x)) / (x**2))
x = 0.0000001; print((1 - cos(x)) / (x**2))
print()
print("My guess was incorrect- limit= 0.5")


