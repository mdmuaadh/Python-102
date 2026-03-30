# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name:Muaadh Mohideen
# Section:ENGR 102-559
# Assignment:Lab 11 Individual
# Date:11/02/2025

#get the inputs
name_file= input("Enter the output filename: ")
principal=float(input("Enter the principal amount: "))
num_months= int(input("Enter the term length (months): "))
interest_rate_year= float(input("Enter the annual interest rate: "))

#calculate the monthly payment 
interest_rate_month= interest_rate_year/12
monthly_payment=(principal * interest_rate_month)/(1-(1/(1+interest_rate_month))**num_months)
#csv file 
balance= principal
interest_tot=0.0

f= open(name_file, "w")
f.write( "Month,Total Accrued Interest,Loan Balance\n")
f.write(f"0,$0.00,${balance:.2f}\n")
#loop 
month = 1
while balance > 0.01:
    interest = balance* interest_rate_month
    interest_tot +=interest
    balance = balance + interest- monthly_payment
    if balance < 0:
        balance = 0.0
    f.write(f"{month},${interest_tot:.2f},${balance:.2f}\n")
    month += 1

f.close()

