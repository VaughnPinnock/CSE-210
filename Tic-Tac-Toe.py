# Week 2 Solo Code
# by Vaughn Pinnock



# initiates the board as a list and adds numbers for each square on the board
def make_board():
    board = []
    for square in range(9):
        board.append(square +1)
    return board


# displays the board using the index of the board list
def draw_board(board):
    print()
    print (f'{board[0]}|{board[1]}|{board[2]}')
    print ('-+-+-+-+-')
    print (f'{board[3]}|{board[4]}|{board[5]}')
    print ('-+-+-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')

#checks for a draw
def is_drawn(board):
    for square in range(9):
        if board[square] != 'x' and board[square] != 'o':
            return False
    return True

#checks for a winner 
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8])

# gets a selection from a player
def player_choice(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

# alternates choice between 'x' and 'o' 
def other_player(current):
    if current == '' or current == 'o':
        return 'x'
    elif current == 'x':
        return 'o'


def main():
    player = other_player('')
    board = make_board()
    while not (winner(board) or is_drawn(board)):
        draw_board(board)
        player_choice(player, board)
        player = other_player(player)
    draw_board(board)

if __name__ == "__main__":
    main()


# def x_choice():
#     ans = int(input("X's turn to choose a square (1-9): "))
#     return ans

# def o_choice():
#     ans = int(input("O's turn to choose a square (1-9): "))
#     return ans

# x = 0

# while True:
#     draw_board()
#     x_choice()
#     draw_board()
#     o_choice()
    


    


