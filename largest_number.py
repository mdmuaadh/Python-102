# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: ENGR 102-559
# Assignment: Lab 4 - Activity 1
# Date: 09/12/25


#Variables Defined From User Input
number1=float(input("Enter number 1:"))
number2=float(input("Enter number 2:"))
number3=float(input("Enter number 3:"))

#Set the equation to see which number is the largest 
#firstly check if num1 largest
if number1 >=  number2 and number1 >=  number3:
    largest=number1
elif number2 >=  number1 and number2 >=  number3:
    largest=number2
else:
    largest = number3

#print the largest number 
print("The largest number is", largest)



