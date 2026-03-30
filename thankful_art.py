# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jose Mina Velasco
#               Mayreli Campos
#               Muaadh Mohideen
# Section:      ENGR 102-559
# Assignment:   TEAM LAB 13 - THANKFUL ART
# Date:         11/18/2025
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import turtle as t


def backendcolor_setup():
    """
    Set up the screen size and background color (11x17 card).
    """
    screen = t.Screen()
    screen.title("Happy Thanksgiving - Team 9")
    screen.bgcolor("lightblue")
    screen.setup(width=1100, height=1700)
    return screen


def cloud1_puff(x, y, size):
    """
    Draw one cloud puff x and y tweak using circles(intertwined)
    """
    t.color("white")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()


def background_color():
    """
    Draw background clouds
    """
    t.speed(0)
    t.hideturtle()

    # 3 circle cloud 
    left_center_x =-400 #CHANGE TO FIT from 400- to near -300
    left_center_y =190
    for i in range(3):
        cloud1_puff(left_center_x + i * 40, left_center_y, 40)

  


def tot_banner():
    """
    Draw Top and Bottom Banner with Text.
    """
    t.color("black", "white")
    # top 
    t.penup()
    t.goto(-250, 400)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(500)
        t.right(90)
        t.forward(90)
        t.right(90)
    t.end_fill()
    t.penup()

    # banner 
    t.color("black")  #white-ChANGE
    t.goto(0, 355)
    t.write("Happy Thanksgiving!", align="center",
            font=("Arial", 28, "bold"))

    # bottom box
    t.color("black", "white")
    t.penup()
    t.goto(-200, -430)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(80)
        t.right(90)
    t.end_fill()
    t.penup()

    # bottom text - fix to fit 475ish
    t.color("black")                
    t.goto(0, -475)
    t.write("From: Team 9", align="center",
            font=("Arial", 20, "normal"))
    t.penup()


def thankful_msg():
    """
    Print what each person is thankful for.
    """
    print("Muaadh is thankful for his loving family and friends.")
    print("Jose is thankful for good health and opportunities.")
    print("Mayreli is thankful for education and happiness.")
    print("......................................................")
    print("Happy Thanksgiving")


def main():
    """
    Person 1 main: setup, background, banner, console text.
    """
    backendcolor_setup()
    background_color()
    tot_banner()
    thankful_msg()

    # Person 2 can call their turtle art here later.
    
    t.done()


main()
