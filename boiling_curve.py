# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"    
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohidee
# Section: Engr - 102 - 559
# Assignment: Lab 5 - Part 2
# Date: 09/18/2025

#Import Log due to the fit the curve
from math import log
#Ask for the input
excessive_temp_in= float(input("Enter the excess temperature: "))

#Define variables of temperatures 
A = (1.3, 1000)
B = (5.0, 7000)
C = (30.0, 1.5e6)
D = (120.0, 2.5e4)
E = (1200.0, 1.5e6)

#Not in range of of the ouputs output as not available 
if excessive_temp_in <1.3 or excessive_temp_in> 1200:
    print("Surface heat flux is not available") 
    #Input plug into one of the four segments
    #A-B
elif A[0] <= excessive_temp_in <= B[0]:
    m=log(B[1]/A[1])/log(B[0]/A[0])
    excess_temp_out=A[1]*(excessive_temp_in/A[0])**m
    print(f"The surface heat flux is approximately {excess_temp_out:.0f} W/m^2")
    #B-C
elif B[0] <= excessive_temp_in <= C[0]:
    m=log(C[1]/B[1])/log(C[0]/B[0])
    excess_temp_out=B[1]*(excessive_temp_in/B[0])**m
    print(f"The surface heat flux is approximately {excess_temp_out:.0f} W/m^2")
    #C-D
elif C[0] <= excessive_temp_in <= D[0]:
    m=log(D[1]/C[1])/log(D[0]/C[0])
    excess_temp_out=C[1]*(excessive_temp_in/C[0])**m
    print(f"The surface heat flux is approximately {excess_temp_out:.0f} W/m^2")
    #D-E
else: 
    m=log(E[1]/D[1])/log(E[0]/D[0])
    excess_temp_out=D[1]*(excessive_temp_in/D[0])**m
    print(f"The surface heat flux is approximately{excess_temp_out:.0f}W/m^2")
