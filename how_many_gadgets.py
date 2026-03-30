    # By submitting this assignment, I agree to the following:
    # "Aggies do not lie, cheat, or steal, or tolerate those who do"
    # "I have not given or received any unauthorized aid on this assignment"
    #
    # Name: Muaadh Mohideen
    # Section: ENGR 102-559
    # Assignment: Lab 4 - Activity 2
    # Date: 09/12/25

#Sum of Arithmetic Sequence 
#Sn= n/2(2a+(n-1)d)

#Input Request from User 
day= int(input("Please enter a positive value for day:\n"))

#Check if it is a negative number if print error

#Four Diffrent Sums Equations and Analyzation from time period 
if day < 0:
    print("You entered an invalid number!")
elif 1<= day <=10:
    n=day
    d=0
    a=10
    produced=n/2* (2*a+(n-1)*d)
    print(f"The sum total number of gadgets produced on day {day} is {int(produced)}")
elif 11<=day<=50:
    n=day -10
    d=1
    a=11
    produced= n/2* (2*a+(n-1)*d) + 10/2 * (2*10 + (10-1)*0)
    print(f"The sum total number of gadgets produced on day {day} is {int(produced)}")
elif 51<=day<=100:
    n=day-50
    a=50
    d=0
    produced= n/2* (2*a+(n-1)*d) + (10/2* (2*10 + (10-1)*0)) + (40/2* (2*11 + (40-1)*1)) 
    print(f"The sum total number of gadgets produced on day {day} is {int(produced)}")
else: 
    produced=3820
    print(f"The sum total number of gadgets produced on day {day} is {int(produced)}") 


