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
# Assignment: Lab 8 Team project planner
# Date: 12-10-2025        

#defines the dictionary containing all of the characters that may be used
digits = {
    '0': ["###", "# #", "# #", "# #", "###"],
    '1': [" # ", "## ", " # ", " # ", "###"],
    '2': ["###", "  #", "###", "#  ", "###"],
    '3': ["###", "  #", "###", "  #", "###"],
    '4': ["# #", "# #", "###", "  #", "  #"],
    '5': ["###", "#  ", "###", "  #", "###"],
    '6': ["###", "#  ", "###", "# #", "###"],
    '7': ["###", "  #", "  #", "  #", "  #"],
    '8': ["###", "# #", "###", "# #", "###"],
    '9': ["###", "# #", "###", "  #", "###"],
    ':': [" ", ":", " ", ":", " "],
    'A': [" A ", "A A", "AAA", "A A", "A A"],
    'P': ["PPP", "P P", "PPP", "P  ", "P  "],
    'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"]
}

time_input = input("Enter the time: ") #takes user input to find time
clock_type = input("Choose the clock type (12 or 24): ") #takes user input to find format
valid_chars = "abcdeghkmnopqrsuvwxyz@$&*=" #defines list of valid characters to print
char = input("Enter your preferred character: ") #takes user input of users preferred character

#checks to see if the user wants to use a specific character
if char == "":
    char = None
else: 
    #checks to see if the users preferred character is in the valid characters
    while True:
        #if the character is not in the valid characters list it prompts user for a new input
        if char not in valid_chars:
            char = input("Character not permitted! Try again: ")
        else:
            break

#finds the hour and minute values
if len(time_input) == 5:
    hour = int(time_input[:2])
    minute = time_input[3:]
elif len(time_input) == 4:
    hour = int(time_input[:1])
    minute = time_input[2:]
    
#defines the variable that will be defined as AM or PM
period = ""

#checks to see if the clocks format will be in 12 hour format
if clock_type == "12":
    #if the clock is in 12 hour format and the hour equals 0 the time period would be AM and would start with '12'
    if hour == 0:
        hour = 12
        period = "AM"
    #if the clock is in 12 hour format and the hour equals 12 the time period would be PM
    elif hour == 12:
        period = "PM"
    #if the clock is in 12 hour format and the hour is greater than 12 the time period would be PM and it switches the value to the 12 hour format
    elif hour > 12:
        hour -= 12
        period = "PM"
    #if the clock is in 12 hour format and the hour is less than 12 the time period will be AM
    else:
        period = "AM"

#makes the clock display hours and minutes with the correct number of digits and space between them
display = f"{hour}:{minute:02}"

#if the format of the clock is 12 hours then it adds the AM or PM to the end of the displayed time
if period:
    display += period

#defines the list of all of the lines that will be printed
lines = ["", "", "", "", ""]

#loops for each character in the display
for i in display:
    art = digits[i] #finds the template for the character
    for j in range(5):
        symbol = i if char is None else char #finds which symbol/number should be used for each character, either users preference or the default
        if lines[j]: #adds the spaces between the characters 
            lines[j] += " "
        lines[j] += art[j].replace("#", symbol) #replaces the '#' in the template with the correct symbol/number
        
#prints all of the lines in the clock
print()
for line in lines:

    print(line)

