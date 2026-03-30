# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: ENGR 102 - 559
# Assignment: Lab 9
# Date: 10/19/2025

from math import *
#Part A

def parta(int_num):
    length= len(int_num)
    between=int_num[:]
    between.sort()
#now solve for both parralels after you get it in order 
    middle=length // 2
    if length % 2 == 1:
        median= between[middle]
        # now calculate median if statemtent is true 
    else:
        median= (between[middle-1]+ between[middle]) / 2
    minimum= min(int_num)
    maximum= max(int_num)
    return (minimum, median, maximum)
 
 #Part B 
def partb (time,distance):
    velocity=[]
    i =0
    #run a while loop to return it (faster)
    while i <len(time)-1:
        velocity.append((distance[i+1]-distance[i]) / (time[i+1]-time[i]))
        i += 1
    return velocity

#Part C
def partc(list_nums):
    list_nums.sort()
    i=0
    length= len(list_nums)-1
    #calculation to see if it goes to 2029
    while i < length:
        s=list_nums[i]+list_nums[length]
        if s ==2029:
            return list_nums[i]*list_nums[length]
        elif s < 2029:
            #chcek all dont leave after one of infinite loop 
            i+=1
        else:
            length = length-1
    return False    

#Part D 
def partd(n):
      #For in range if not break and return false if only the calc works 
      for start in range(2,n, 2):
        total = 0
        num = []
        for x in range(start, n, 2):
            total += x
            num.append(x)  
            if len(num) >= 2 and total == n:
                return num
            if total > n:
                break
      return False

#Part E
def parte(Radius_S, Radius_H):
    if Radius_S <=0 or Radius_H<0 or Radius_H>Radius_S:
        return False
    #Calculations  
    half= (Radius_S*Radius_S- Radius_H*Radius_H) ** 0.5 
    height= 2*half 
    height_cap= Radius_S -half 
    Vol_Sphere= (4.0/3.0)* pi *(Radius_S**3)
    Vol_Cap= (pi*(height_cap**2) *(3*Radius_S - height_cap))/ 3.0
    Vol_drill = pi * (Radius_H**2) * height
    f_vol = Vol_Sphere - (2*Vol_Cap + Vol_drill)
    return f_vol

#Part F     
def partf(border, name, company, email):
    maximum = max(len(name), len(company), len(email))
    padding = 2
    space = " "* padding
    inside = maximum + 2*padding
    width = inside + 2
    top = border * width
    #Double Check (I think i messed up with the width )
    def row(text):
        diff=maximum - len(text)
        left=diff // 2
        right=diff - left
        return border + space + (" " * left) +text +(" " * right) +space+border
    row_1 = row(name)
    row_2 = row(company)
    row_3 = row(email)
    return top + "\n" + row_1 + "\n" + row_2 + "\n" + row_3 + "\n" + top
#Part G
def partg(val, tolerance):
    if val<=-1 or val>=1 or tolerance <=0:
        return False
    #after false return total calculation 
    total =0.0
    n=1
    term_input= val
    while True:
        term = (2.0 / n) * term_input
        if abs(term) < tolerance:
            break
        total += term
        term_input=term_input*val* val 
        n +=2
    return total