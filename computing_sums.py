# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: Engr 102-559
# Assignment: Lab 6 Activity 1
# Date: 09/28/2025

integer_1=int(input("Enter an integer:"))
integer_2=int(input("Enter another integer:"))
#if first number is greater than second number 
integer_1_min= min(integer_1, integer_2)
integer_2_max= max(integer_1, integer_2)
   
#calculate 
total=0
for i in range(integer_1_min, integer_2_max+1):
    total+=i
#print the result
print("The sum of all integers from", integer_1, "to", integer_2, "is", total)



