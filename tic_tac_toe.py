import subprocess
subprocess.run('cls',shell=True)
class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " "," "]

    def display(self):
        print(" {0} | {1} | {2} ".format(self.cells[0],self.cells[1],self.cells[2]))
        print("------------------")
        print(" {0} | {1} | {2} ".format(self.cells[3], self.cells[4], self.cells[5]))
        print("------------------")
        print(" {0} | {1} | {2} ".format(self.cells[6], self.cells[7], self.cells[8]))

    def update_cell(self,cell_no,player):
        if self.cells[cell_no-1] == " ":
            self.cells[cell_no - 1] = player


    def is_winner(self,player):
        if self.cells[0] == player and self.cells[1] == player and self.cells[2] == player:
            return True
        if self.cells[3] == player and self.cells[4] == player and self.cells[5] == player:
            return True
        if self.cells[6] == player and self.cells[7] == player and self.cells[8] == player:
            return True
        if self.cells[0] == player and self.cells[3] == player and self.cells[6] == player:
            return True
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[0] == player and self.cells[4] == player and self.cells[8] == player:
            return True
        if self.cells[2] == player and self.cells[4] == player and self.cells[6] == player:
            return True
        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset_board(self):
        self.cells = [" "," "," "," "," "," "," "," "," "]
        return self.cells

board = Board()

def print_header():

    print("Welcome to Tic-Tac-Toe\n")

def refresh_screen():
    #Clear the Screen
    subprocess.run('cls',shell=True)
    #Print the Header
    print_header()
    #Show the board
    board.display()

while True:
    refresh_screen()

    #Get the X input
    x_choice = int(input("\nX) please choose 1-9.> "))
    if x_choice in range(1,10):
        #Update Board
        board.update_cell(x_choice,"X")
        # check for 'X' wins
        if board.is_winner("X"):
            print("\nX wins\n")
            play_again = input("Would you like to play again (Y/N) >").upper()
            if play_again == 'Y':
                board.reset_board()
            else:
                break
        # check for 'Tie' Game
        if board.is_tie():
            print("\n Tie Game!\n")
            play_again = input("Would you like to play again (Y/N) >").upper()
            if play_again == 'Y':
                board.reset_board()
            else:
                break
    else:
        print("Entered Wrong Number")
        break



    refresh_screen()
    #Get the O input
    o_choice = int(input("\nO) please choose 1-9.> "))
    if o_choice in range(1,10):
        #Update Board
        board.update_cell(o_choice,"O")
        # Check for 'O' Wins
        if board.is_winner("O"):
            print("\n O Wins\n")
            play_again = input("Would you like to play again (Y/N) > ").upper()
            if play_again == 'Y':
                board.reset_board()
            else:
                break

        # check for 'Tie' Game
        if board.is_tie():
            print("\n Tie Game!\n")
            play_again = input("Would you like to play again (Y/N) >").upper()
            if play_again == 'Y':
                board.reset_board()
            else:
                break

    else:
        print("Entered wrong number")
        break






