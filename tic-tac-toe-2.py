import random

board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
game_playing = True

# take user's marker choice

user_marker = "X"

# create the game board


def show_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("------------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("------------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print("------------")


# take user input

def user_input(board):
    position = int(input("Please input a number 1-9 :"))

    if board[position-1] == "_":
        board[position-1] = user_marker

    else:
        print("Oops, please input a valid position number.")


# chech win


def row_check(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True


def hor_check(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[3]
        return True
    elif board[2] == board[3] == board[8] and board[2] != "_":
        winner = board[2]
        return True


def line_check(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True


def check_win():
    global game_playing
    if row_check(board) or hor_check(board) or line_check(board):
        print(f"The winner is {winner}! ")
        game_playing = False


# check tie
def check_tie(board):
    global game_playing
    if "_" not in board:
        show_board(board)
        print("It's a Tie.")
        game_playing = False


# switch user

def switch_user():
    global user_marker
    if user_marker == "X":
        user_marker = "O"
    else:
        user_marker = "X"


# create computer player
def computer_player(board):
    while user_marker == "O":
        com_position = random.randint(0, 9)
        if board[com_position] == "_":
            board[com_position] = "O"
            switch_user()


# check win again

while game_playing:
    show_board(board)
    user_input(board)
    check_win()
    check_tie(board)
    switch_user()
    computer_player(board)
    check_win()
    check_tie(board)
