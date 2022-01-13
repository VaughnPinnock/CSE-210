"""
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
If all nine squares are full and neither player has three in a row, the game ends in a draw.


Your program must also meet the following requirements.

The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main.

"""

class Board():
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        
    def display(self):
        print (f'{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')
        print ('-+-+-+-+-')
        print (f'{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print ('-+-+-+-+-')
        print (f'{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')

    def update_move(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        if self.cells[1]== player and self.cells[2]==player and self.cells[3]==player:
            return True

        if self.cells[4]== player and self.cells[5]==player and self.cells[6]==player:
            return True

        if self.cells[7]== player and self.cells[8]==player and self.cells[9]==player:
            return True

        if self.cells[1]== player and self.cells[4]==player and self.cells[7]==player:
            return True

        if self.cells[2]== player and self.cells[5]==player and self.cells[6]==player:
            return True

        if self.cells[3]== player and self.cells[6]==player and self.cells[9]==player:
            return True

        if self.cells[1]== player and self.cells[5]==player and self.cells[9]==player:
            return True

        if self.cells[3]== player and self.cells[5]==player and self.cells[7]==player:
            return True
        
        return False

    def is_draw(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False
         
board = Board()

def print_header():
    print('Welcome to CS210 TIC-TAC-TOE\n')

def refresh_screen():
    # print_header()

    
    board.display()


def main():

    
    while True:

        # refresh screen
        refresh_screen()

        # gets user choice
        x_choice = int(input("\nx's turn to choose a square (1-9): "))

        # update board
        board.update_move(x_choice, 'X')

        # refresh screen
        refresh_screen() 

        # check for an x winner
        if board.is_winner('X'):
            print ('\nX wins!')
            break
        
        # check for an O winner
        if board.is_winner('O'):
            print ('\n0 wins!')
            break
            
        if board.is_draw():
            print ('\nTie Game\n')
            break



        # gets user choice
        o_choice = int(input("\nO's turn to choose a square (1-9): "))

        # updates board
        board.update_move(o_choice, '0')

        # check for an x winner
        if board.is_winner('X'):
            print ('\nX wins!')
            break
        
        if board.is_winner('O'):
            print ('\n0 wins!')
            break


  
    

if __name__ == "__main__":
    main()

    