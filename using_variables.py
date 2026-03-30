# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Muaadh Mohideen
# Section: ENGR 102 - 559
# Assignment: Lab 2 : Topic 1
# Date: 09/2/2025
#

#Reynolds Number (Part A)
#Calculating and printing Re Number (dimensionless quantity in fluid mechanics that is used to predict flow patterns in different fluid flow situations )
#velocity 9 m/s and kinematic_viscosity 0.0015 m^2/s and char_dimension of 0.875 m
velocity= 9 
kinematic_viscosity= 0.0015
char_dimension= 0.875
#Work 
Re = (velocity*char_dimension) / kinematic_viscosity
#Full Form of Answer 

print("Reynolds number is", Re)

from math import sin, log, pi 
#Braggs Law (Part B)
#Calculate and print the wavelength of x-rays scattering from a crystal lattice 
#distance 0.029 nm , angle (deg), diffraction (n)
distance= 0.029
angle= 35
diffraction=1
#degrees to radians 
deg_rad = angle * (pi/180)
#Equation (Divided by n to get it to the other side) and solve 
wavelength = (2 * distance * sin(deg_rad)) /diffraction
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
qt = qi / ((1 + b*di*t) ** (1/b))
#Full form 
print ("Production rate is", qt, "barrels/day")

#Tsiolkovsky rocket equation (Part D)
#Calculate  the motion of a device that can apply acceleration to itself by expelling part of its mass with high velocity and print the Tsiolkovsky rocket equation answer
#Initial mass 11000kg , final mass of 8300kg , exhaust velocity 2029 m/s, natural log (ln)
initial_mass= 11000
final_mass=8300
exhaust_velocity=2029 
#Equation to solve q(t)
change_velocity= exhaust_velocity * log(initial_mass/final_mass)
#Full form
print("Change of velocity is", change_velocity, "m/s")    
