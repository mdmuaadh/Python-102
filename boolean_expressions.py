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
# Assignment: Lab 4-4.21
# Date: 16-09-2025
#
############ Part A ############
ainp = input("Enter True or False for a: ") #input for variables
binp = input("Enter True or False for b: ")
cinp = input("Enter True or False for c: ")

a= ainp in ('True', 't', 'T', 'true') # coverts inputs into boolean expressions
b= binp in ('True', 't', 'T', 'true')
c= cinp in ('True', 't', 'T', 'true')
############ Part B ############
exp1 = a and b and c #evaluates expressions into true/false
exp2 = a or b or c

print(f'a and b and c: {exp1}') #prints the result
print(f'a or b or c: {exp2}')
############ Part C ############
exp3 = (a and not b) or (not a and b) # converts booleans for XOR
exp4 = (a and not b and not c) or  (not a and b and not c) or (not a and not b and c) or (a and b and c) #converts for odd numbers of true and false

print(f'XOR: {exp3}') #prints out XOR and odd number
print(f'Odd number: {exp4}')
############ Part D ############
#First complex expresion and its simplified first
exp5 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
exp5S = (not b) or (not a and not c)

# evaluates 2nd expression and its simplified version
exp6 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or
(a and b and c) or (a and ((b and not c) or (not b))))
exp6S = a or (not b and c)

print(f'Complex 1: {exp5}') 
print(f'Complex 2: {exp6}')
print(f'Simple 1: {exp5S}')
print(f'Simple 2: {exp6S}')