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
# Assignment: Lab 4 Team Optional 
# Date: 07-09-2025



# program a code that prints the quadratic eq Ax^2 + Bx + C = 0
# and if given coefficients are either 0 or 1, they won't print
# and if -1 the variable will print with a changed sign
# prompt input from the user
A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))

terms = []

# set conditional for A
if A != 0:
    if A == 1:
        terms.append('x^2')
    elif A == -1:
        terms.append('- x^2')
    else:
        terms.append(f'{A:+}x^2' if terms else f'{A}x^2')

# Hset conditional for B
if B != 0:
    sign = '+ ' if B > 0 else '- '
    abs_value = abs(B)
    if abs_value == 1:
        term = 'x'
    else:
        term = f'{abs_value}x'
    if terms:
        terms.append(f'{sign}{term}')
    else:
        terms.append(f'- {term}' if B < 0 else term)

# set conditional for c
if C != 0:
    sign = '+ ' if C > 0 else '- '
    abs_value = abs(C)
    if terms:
        terms.append(f'{sign}{abs_value}')
    else:
        terms.append(f'- {abs_value}' if C < 0 else str(abs_value))

# put it all together for the final print statement
equation = ' '.join(terms) + ' = 0'

print(f'The quadratic equation is {equation}')