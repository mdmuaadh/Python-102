# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Muaadh Mohideen
# Section: ENGR 102 - 559
# Assignment: Lab 3 : Topic 1
# Date: 09/08/2025
#Reynolds Number (Part A)
#Calculating and printing Re Number (t dimensionless quantity in fluid mechanics that is used to predict flow patterns in different fluid flow situations )
#velocity (𝑢) 9 m/s and kinematic viscosity (𝜈) 0.0015 m^2/s and characteristic linear dimension (L) of 0.875 m
print("This program calculates the Reynolds number given velocity, length, and viscosity")

u= float(input("Please enter the velocity (m/s): "))
L= float(input("Please enter the length (m):"))
v= float(input("Please enter the viscosity (m^2/s):"))


#Work 
Re = (u*L) / v
#Full Form of Answer 

print(f"Reynolds number is {Re:.0f}")

from math import sin, log, pi 
#Braggs Law (Part B)
#Calculate and print the wavelength of x-rays scattering from a crystal lattice 
#Distance between crystal layers 0.029 nm (d), Scattering angle of 35 degrees (deg), first (1) order diffraction (n)
print("This program calculates the wavelength given distance and angle")
d= float(input("Please enter the distance (nm): "))
deg= float(input("Please enter the angle (degrees):"))
n=1
#degrees to radians 
deg_rad = deg * (pi/180)
#Equation (Divided by n to get it to the other side) and solve 
wavelength = (2 * d * sin(deg_rad)) /n
#Full form
print(f"Wavelength is {wavelength:.4f} nm")

#Arps Equations (Part C)
#calculate to forecast future production rates of oil and gas wells after 10 days and print the answer 
#Initial production rate 100 barrels/day (qi), initial decline rate 2/day (di), hyperboliic constant 0.8 (b), Time 10 (t)
print("This program calculates the production rate given time, initial rate, and decline rate")
t=  float(input("Please enter the time (days):"))
qi= float(input("Please enter the initial rate (barrels/day):"))
di= float(input("Please enter the decline rate (1/day): "))

b=0.8
#Equation to solve q(t) which is the forecast / arps equation
qt = qi / ((1 + b * di * t) ** (1/b))
#Full form 
print (f"Production rate is {qt:.2f} barrels/day")

#Tsiolkovsky rocket equation (Part D)
#Calculate  the motion of a device that can apply acceleration to itself by expelling part of its mass with high velocity and print the Tsiolkovsky rocket equation answer
#Initial mass 11000kg (mo), final mass of 8300kg (mf), exhaust velocity 2029 m/s (ve), natural log (ln)
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
mo= float(input("Please enter the initial mass (kg):"))
mf= float(input("Please enter the final mass (kg): "))
ve= float(input("Please enter the exhaust velocity (m/s): "))
#Equation to solve q(t)
cvelocity= ve * log(mo/mf)
#Full form
print(f"Change of velocity is {cvelocity:.1f} m/s")
