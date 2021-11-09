"""
Name: Caroline Greer
lab10.py

Discription: Solve the problems for lab 10

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

def create_board():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board

def draw_board(board):
    value = board
    print(value[0] + " | " + value[1] + " | " + value[2], end="\n")
    print("---------")
    print(value[3] + " | " + value[4] + " | " + value[5], end="\n")
    print("---------")
    print(value[6] + " | " + value[7] + " | " + value[8], end="\n")


def mark_space(board, position, character):
    character = character.upper()
    if character == "X" or character == "O":
        board[int(position) - 1] = character
    else:
        print("check your input")


def spot_valid_test(board, position):
    number = board[int(position)-1]
    return number.isnumeric()


def game_winner_test(board):
    value = board
    if value[0] == value[1] == value[2]:
        return True
    elif value[3] == value[4] == value[5]:
        return True
    elif value[6] == value[7] == value[8]:
        return True
    elif value[0] == value[4] == value[8]:
        return True
    elif value[2] == value[4] == value[6]:
        return True
    elif value[5] == value[7] == value[8]:
        return True
    elif value[0] == value[3] == value[6]:
        return True
    elif value[1] == value[4] == value[7]:
        return True
    elif value[2] == value[5] == value[8]:
        return True
    else:
        return False


def game_over_test(board):
    if game_winner_test(board):
        return True
    else:
        for i in range(len(board)):
            open = str(board[i]).isnumeric()
            if open:
                return False
        return True


def main():
    print("Welcome to TicTacToe! You and your opponent will be playing a competitive game of TicTacToe, " +
    "with one player being 'x' " +
    "and the other character being 'o'. Choose who will go first and let's start the game!")
    board = create_board()
    draw_board(board)
    player = 1
    while not game_over_test(board):
        player = player * -1
        if player == -1:
             str_player = "Player 1"
        else:
             str_player = "Player 2"
        move = input("Input your move " + str_player + " as position space character: ")
        position, character = move.split(" ")
        if spot_valid_test(board, position):
            mark_space(board, position, character)
            draw_board(board)
        else:
            print("input value again")
            player = player * -1
    while game_over_test(board):
        if player == -1:
            print("Player 1 wins!")
            return
        elif player == 1:
            print("Player 2 wins!")
            return
        else:
            print("Tie")
            return
    pass

main()
