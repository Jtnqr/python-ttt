# TODO:
#     - add draw

import os

play = True
winner = ''
turn = 'X'
moves = 0
user = {0: ' ', 1: 'X', 2: 'O'}
yes = {'yes','y', 'ye', ''}
no = {'no','n'}
q = {'quit','q'}
r = {'reset','r'}
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def display_game(error=0):
    j = 0

    clear()
    print(moves)
    print(' ' * 12 + "TicTacToe")
    print('>' + '-' * 31 + '<')
    print("Inputs:")
    print("- Number 1-9")
    print("- q to quit")
    print("- r to reset")
    print('>' + '-' * 31 + '<')

    # Print board
    for i in range(3):
        if i == 1:
            j = 3
        elif i == 2:
            j = 6
        print("[ {} ][ {} ][ {} ] ! [ {} ][ {} ][ {} ]".format(board[i][0],board[i][1],board[i][2],j+1,j+2,j+3))
    
    print('>' + '-' * 31 + '<')
    print("Current turn :", turn)

    if error == 1:
        print("Incorrect input!")
    elif error == 2:
        print("Already filled!")

def run_game():
    global play, turn
    whose = moves % 2 + 1
    
    display_game()
    turn = 'X' if moves % 2 != 0 else 'O'

    while True:
        board = input("> ")

        if board.lower() in q:
            play = False
            break
        elif board.lower() in r:
            reset_game()
            break
        elif board.isdigit() and int(board) in range(1,10):
            if change_board(whose, int(board)):
                break
            else:
                # turn = 'O' if moves % 2 != 0 else 'X'
                display_game(2)
                continue
        else:
            display_game(1)
            
def change_board(whose, num):
    global moves

    if num in (1,2,3):
        if board[0][num-1] == ' ' or whose == 0:
            board[0][num-1] = user[whose]
        else:
            return False
    elif num in (4,5,6):
        if board[1][num-4] == ' ' or whose == 0:
            board[1][num-4] = user[whose]
        else:
            return False
    elif num in (7,8,9):
        if board[2][num-7] == ' ' or whose == 0:
            board[2][num-7] = user[whose]
        else:
            return False
    
    if whose != 0:
        moves += 1

    return True

def check_win():
    for i in range(3):
        # Row check win
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ':
            end_game()
        # Column check win
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
            end_game()
    # Diagonal check win
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        end_game()
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        end_game()

    # Draws check
    if moves == 9:
        end_game(False)

def end_game(win=True):
    global winner, play

    if moves % 2 != 0:
        winner = 'X'
    else:
        winner = 'O'

    display_game()

    if win:
        print("The game has ended, the winner is {}!".format(winner))
    else:
        print("The game has ended, the game is draw!")

    while True:
        retry = input("Retry?[Y/n] ").lower()
        if retry in yes:
            reset_game()
            break
        elif retry in no:
            play = False
            break
        else:
            print("Choices are (y)es/(n)o")

def reset_game():
    global winner, moves
    winner = ''
    moves = 0
    
    for i in range(10):
        change_board(0,i)

while play:
    run_game()
    check_win()