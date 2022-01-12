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
boardvalues = { '1':'', '2':'', '3':'',
                '4':'', '5':'', '6':'',
                '7':'', '8':'', '9':'',
}

def printboard():
    print ('1' + '|' + '2' + '|' + '3')
    print ('-+-+-+-')
    print ('4' + '|' + '5' + '|' + '6')
    print ('-+-+-+-')
    print ('7' + '|' + '8' + '|' + '9')


def main():
    printboard()

if __name__ == "__main__":
    main()

    