# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: 
# Jacob Gil
# Michael Mendoza
# Muaadh Mohideen (Project manager)
# Xander Tivis
# Section: ENGR - 102 - 559
# Assignment: Lab 7 Team project planner
# Date: 7-10-2025

#defines all of the lists used and other variables
empty = '.'
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []
board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

#creates to boards blank spaces '.'
for i in range(9):
    row1.append(empty)
    row2.append(empty)
    row3.append(empty)
    row4.append(empty)
    row5.append(empty)
    row6.append(empty)
    row7.append(empty)
    row8.append(empty)
    row9.append(empty)

#function to print the board for each move
def print_board():
    for i in board:
        print(' '.join(i))
    print()

#sets the turn at the start of the game
turn_black = True

#prints the format for the stone placements and prints the board
print("Type coordinates like 'row col' (for example: 3 5) or type 'stop' to end.")
print_board()

while True:
    #Checks which players turn it is and saves which tile should be used
    if turn_black:
        stone = 'O'
        player = "Black"
    else:
        stone = 'o'
        player = "White"
    #Collects the users input and checks whether it is valid or will end the game
    move = input(f"{player}'s move (row col) or 'stop': ")
    if move.lower() == "stop":
        print("Game ended")
        break
    parts = move.split()
    if len(parts) != 2:
        print("Please enter row and column numbers separated by a space.")
        continue
    #defines which row and column the users input is
    row = int(parts[0]) - 1
    col = int(parts[1]) - 1
    #checks to see if users input fits on the board
    if row < 0 or row > 8 or col < 0 or col > 8:
        print("Coordinates out of range! Use numbers 1–9.")
        continue
    #checks to see if the tile is empty or not and reports an error if it is full
    if board[row][col] != empty:
        print("That spot is already taken. Try again.")
        continue

    #adds the users input to the board
    board[row][col] = stone
    #prints the new board
    print_board()
    #switches turns
    turn_black = not turn_black