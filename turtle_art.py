# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: ENGR 102- 559
# Assignment: Lab 13 Individual - Turtle Art
# Date: 11/16/2025

import turtle as t
from math import *

#part A
def parta(angle):
    '''
    draw figure based on turning angle till it reaches back to to the start point
    '''
    t.dot (10,"red")

    #turn count
    turn_tot=0
    turn=0
    while True:
        turn_tot+=angle
        turn+=1
        if turn_tot % 360==0 :
            break
    
    #draw figure
    for i in range (turn):
        t.left(angle)
        t.forward(300)

def partb(fix_angle):
    '''
    use input of 0 and 1 with fixed angle for it to draw figure and come back to start point
    '''
    t.dot(10,"red")
    start = t.position()

    angle_0 = 30
    angle_1 = -114

    # repeat 
    for loops in range(300):   
        for digit in fix_angle:
           
            if digit == '0':
                t.left(angle_0)
            elif digit == '1':
                t.left(angle_1)
            
            t.forward(40)
        if t.distance(start) < 1:
            break


#part C
def partc(spiral, angle0, angle1):
    '''
    spiral drawing  using sequences of 0 and 1 
    '''
                
    t.dot(10,"red")
    step = 3 

    for value in spiral:
        if value == '0':
            t.left(angle0)
        elif value == '1':
            t.left(angle1)
        #move
        t.forward(step)
        step += 1

#Main
#parta-main
parta(160)
input()
t.reset()
#parta-141-main
parta(141)
input()
t.reset()

#partb-main
partb("01001")
input()
t.reset()
#partb2-main
partb("01001011")
input()
t.reset()

#partc-main
spiral1 = ""
for i in range(20):
    spiral1 = spiral1 + "1"
    for j in range(i):
        spiral1 = spiral1 + "0"

partc(spiral1, 0, 90)
input()
t.reset()

partc(spiral1, 0, 30)
input()
t.reset()

# spiral with 50 
spiral2 = ""
for i in range(50):
    spiral2 = spiral2 + "1"
    for j in range(i):
        spiral2 = spiral2 + "0"

partc(spiral2, 0, 150)
input()
t.reset()
partc(spiral2, 5, 108)

t.done()