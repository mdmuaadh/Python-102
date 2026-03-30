# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Michael Mendoza
#               Jacob Gil
#               Xander Tivis
#               Muaadh Mohideen
# Section:      ENGR 102
# Assignment:   LAB 6 TEAM Approximating ln
# Date:         30 September 2025
# import math as we are working with the natural log
import math
# prompt user for input and set variable x
x = float(input('Enter a value for x: '))
while x <= 0 or x > 2:
    x = float(input('Out of range! Try again: '))
# set variable for tolerance and prompt user input for tolerance
toler = float(input('Enter the tolerance: '))
# initialize the variables for the equation approximation
n = 1
term = (x-1) # Beginning term of the ln set
approx_ln = 0.0 #set ln approximation
# loop terms until the following term is lower than the entered tolerance
while abs(term) >= toler:
    approx_ln += term
    n += 1
    term = ((-1) ** (n + 1)) * ((x-1) ** n) /n
# turn approximation into exact value 
exactv_ln = math.log(x)
# have program send output
print(f'ln({x}) is approximately {approx_ln}')
print(f'ln({x}) is exactly {exactv_ln}')
print(f'The difference is {abs(approx_ln - exactv_ln)}')