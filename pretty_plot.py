# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Muaadh Mohideen
# Section:      ENGR 102- 559
# Assignment:   Lab Topic 12 - Pretty Plot
# Date:         11/11/2025

#import mods
import numpy as np
import matplotlib.pyplot as plt

#start vector 
vector = np.array([0, 1])
#start matrix
matrix = np.array([[1.02, 0.095],
                   [-0.095, 1.02]])

# amount for loops 
total =250

# list of x and y (store)
x_points =[]
y_points =[]

# for loop
for i in range(total):
    vector=matrix@vector
    x_points.append(vector[0])
    y_points.append(vector[1])

# plot
plt.plot(x_points, y_points)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Pretty Spiral Plot (Matrix * Vector)")
plt.show()

