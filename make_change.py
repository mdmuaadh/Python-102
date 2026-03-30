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
# Assignment: Lab 4 Team project planner
# Date: 16-09-2025
         

# This program will find how many an which coins are needed to be given as change    

from math import *

# gets inputs from user
pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

# finds how much change should be given
change = round(pay - cost, 2)

# converts the amount of change to whole numbers for easy floor division and modulus
coins = int(round(change * 100))

quarters = coins // 25 # finds the amount of quarters needed 
coins %= 25 # finds the amount of change remaining after removing the amount of quarters
dimes = coins // 10 # finds the amount of dimes from remaining change
coins %= 10 # finds the amount of change remaining after removing the amount of dimes
nickels = coins // 5 # finds the amount of nickels from remaining change
coins %= 5 # finds the amount of change remaining after removing the amount of nickels
pennies = coins # gives the final amount of pennies

print(f"You received ${change:.2f} in change. That is...")

# checks to see if the amount of coins are > 0 and if they are > 1 and prints appropriately
if quarters > 0:
    print(f"{quarters} quarter" + ("s" if quarters > 1 else ""))
if dimes > 0:
    print(f"{dimes} dime" + ("s" if dimes > 1 else ""))
if nickels > 0:
    print(f"{nickels} nickel" + ("s" if nickels > 1 else ""))
if pennies > 0:
    print(f"{pennies} penn" + ("ies" if pennies > 1 else "y"))
