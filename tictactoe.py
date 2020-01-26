
#Global Variable
game_in_progress = True

#create board
board = ['-','-','-',
       '-','-','-',
       '-','-','-']

#show board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#check for winner / tie
def check_for_win():
    global game_in_progress
    #row winners
    if board[0] == board[1] == board[2] != "-":
        display_board()
        print("Player " + board[1] + " wins. ")
        game_in_progress = False
    if board[3] == board[4] == board[5] != "-":
        display_board()
        print("Player " + board[3] + " wins. ")
        game_in_progress = False
    if board[6] == board[7] == board[8] != "-":
        display_board()
        print("Player " + board[6] + " wins. ")
        game_in_progress = False
    #column winners
    if board[0] == board[3] == board[6] != "-":
        display_board()
        print("Player " + board[0] + " wins. ")
        game_in_progress = False
    if board[1] == board[4] == board[7] != "-":
        display_board()
        print("Player " + board[4] + " wins. ")
        game_in_progress = False
    if board[2] == board[5] == board[8] != "-":
        display_board()
        print("Player " + board[5] + " wins. ")
        game_in_progress = False
    #diagonal winners
    if board[0] == board[4] == board[8] != "-":
        display_board()
        print("Player " + board[0] + " wins. ")
        game_in_progress = False
    if board[2] == board[4] == board[6] != "-":
        display_board()
        print("Player " + board[4] + " wins. ")
        game_in_progress = False
    #check for tie
    if game_in_progress == True:
        if "-" not in board:
            game_in_progress = False
            print("It's a tie.")


def play_tic_tac_toe():
    global game_in_progress
    while game_in_progress == True:
        display_board()
        position = input("Player 1 (X), Choose a space between 1-9 ")
        position = int(position) - 1
        board[position] = "X"
        check_for_win()

        if game_in_progress == True:
            display_board()
            position = input("Player 2 (O), Choose a space between 1-9 ")
            position = int(position) - 1
            board[position] = "O"
            check_for_win()


#-------------------------------------------------------------------
play_tic_tac_toe()
