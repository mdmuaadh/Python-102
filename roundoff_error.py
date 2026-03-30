# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: 
# Jacob Gil
# Michael Mendoza
# Muaadh Mohideen
# Xander Tivis
# Section: ENGR - 102 - 559
# Assignment: TEAM CONTRACT
# Date: 07-09-2025
############ Part A ############
# Testing the value of a and if its rounded off. The value of B if no round off should be 1
a=1/7
print(f'a = {a}')
b=a*7
print (f'b = a * 7 = {b}')
#I do see that the value of a is rounded off and I also observed that the value of b is 1 
# Now we are testing the following values and if no round off f should equal one 
c=2*a
d=5*a
f=c+d
print(f'f = 2 * a + 5 * a = {f}')
#After testing I figured out that the value came out to a large number reaching to 1 but dosent touch it because of the round off error
#The values for these as well should be one in both cases 
from math import sqrt
x=sqrt(1/3)
print(f'x = {x}')
y=x*x*3
print(f'y = x * x * 3 = {y}')
z=x*3*x
print(f'z = x * 3 * x = {z}')
#while Y is one and z is apporaching one and is very close such as 0.99999 we see that round off error affected these calculations
############ Part B ############
# check if b and f are equal within specified tolerance
TOL= 1e-10
if abs(b-f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT equal within tolerance of {TOL}')
#Similar tolerance check to the variables z and y 
if abs(y-z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT equal within tolerance of {TOL}')
############ Part C ############
m=0.1
print(f'm = {m}')
n=3*m
print(f'n = 3 * m = 0.3 {n==0.3}')
p=7*m
print(f'p = 7 * m = 0.7 {p==0.7}')
q=n+p   
print(f'q = n + p = 1 {q==1}')
#the values output when stored look exact but the memory of the computer running it can only process binary so its on the basis of approxomations
#n,p, and q all gave false when due to roundoff error.