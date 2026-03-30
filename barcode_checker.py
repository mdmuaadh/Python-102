# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Muaadh Mohideen
# Section: ENGR 102-559
# Assignment: Lab 11 Individual
# Date: 11/02/2025

name_file=input ("Enter the name of the file: ").strip()

with open(name_file,'r') as file:
    barcodes = file.read().splitlines()

barcodes_valid=[]

#loop through the barcodes check if 13 digits
for barcode in barcodes:
    barcode = barcode.strip()
    if len(barcode) != 13 or not barcode.isdigit():
        continue

    #calculate checksum
    first=[int(barcode[i]) for i in range(0, 12, 2)]   
    second=[int(barcode[i]) for i in range(1, 12, 2)]  

    sum1=sum(first)
    sum2=sum(second)
    three_times= sum2*3
    combined= sum1 + three_times
    
    check_calc = 10 - (combined % 10)
# get check digit(compare)
    check_dig = int(barcode[12])

    if check_calc==check_dig:
        barcodes_valid.append(barcode)

    #back to file then output 
with open("valid_barcodes.txt", "w") as out:
    for code in barcodes_valid:
        out.write(code + "\n")

print(f"There are {len(barcodes_valid)} valid barcodes")



    
