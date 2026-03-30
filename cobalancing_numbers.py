# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"                
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: Engr 102-559
# Assignment: Lab 6 Activity 2
# Date: 09/28/2025
#Ask the user for an input
n = int(input("Enter a value for n:"))
#check if the input the user gave is acceptable (positive integer)
if n<= 0:
    print("Please enter a positive integer")
#if it is acceptable calculate both first sum and second sum (diff equation)
else:
    first_sum = 0
    for i in range(1, n + 1):
        first_sum= first_sum + i

    second_sum = 0
    r=0
    while second_sum<first_sum:
        r =r+1
        second_sum+=(n + r)

#with the answer calculation print answer
if first_sum == second_sum:
    print(n,"is a co-balancing number with r =",r)
else:
    print(n,"is not a co-balancing number")
