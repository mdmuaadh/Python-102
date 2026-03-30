# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Muaadh Mohideen
# Section: ENGR 102 - 559
# Assignment: Lab 1 : Topic 2 
# Date: 08/30/2025
#

#Reynolds Number (Part A)
#Calculating and printing Re Number (t dimensionless quantity in fluid mechanics that is used to predict flow patterns in different fluid flow situations )
#velocity (𝑢) 9 m/s and kinematic viscosity (𝜈) 0.0015 m^2/s and characteristic linear dimension (L) of 0.875 m
u= 9 
v= 0.0015
L=0.875
#Work 
Re = (u*L) / v
#Full Form of Answer 

print("Reynolds number is", Re)

from math import sin, log, pi 
#Braggs Law (Part B)
#Calculate and print the wavelength of x-rays scattering from a crystal lattice 
#Distance between crystal layers 0.029 nm (d), Scattering angle of 35 degrees (deg), first (1) order diffraction (n)
d= 0.029
deg= 35
n=1
#degrees to radians 
deg_rad = deg * (pi/180)
#Equation (Divided by n to get it to the other side) and solve 
wavelength = (2 * d * sin(deg_rad)) /n
#Full form
print("Wavelength is", wavelength, "nm")

#Arps Equations (Part C)
#calculate to forecast future production rates of oil and gas wells after 10 days and print the answer 
#Initial production rate 100 barrels/day (qi), initial decline rate 2/day (di), hyperboliic constant 0.8 (b), Time 10 (t)
qi= 100
di=2
b=0.8
t=10
#Equation to solve q(t) which is the forecast / arps equation
qt = 100 / ((1 + 0.8*2*10) ** (1/0.8))
#Full form 
print ("Production rate is", qt, "barrels/day")

#Tsiolkovsky rocket equation (Part D)
#Calculate  the motion of a device that can apply acceleration to itself by expelling part of its mass with high velocity and print the Tsiolkovsky rocket equation answer
#Initial mass 11000kg (mo), final mass of 8300kg (mf), exhaust velocity 2029 m/s (ve), natural log (ln)
mo= 11000
mf=8300
ve=2029 
#Equation to solve q(t)
cvelocity= ve * log(mo/mf)
#Full form
print("Change of velocity is", cvelocity, "m/s")
