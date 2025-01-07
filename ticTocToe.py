from IPython.display import clear_output   

def print_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board,marker,position):
   
    board[position] = marker 

def win_check(board,mark):
   
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #1st row
    (board[4] == mark and board[5] == mark and board[6] == mark) or  # 2nd row
    (board[1] == mark and board[2] == mark and board[3] == mark) or  #3rd row
    (board[7] == mark and board[4] == mark and board[1] == mark) or  #1st column
    (board[8] == mark and board[5] == mark and board[2] == mark) or  #2nd column
    (board[9] == mark and board[6] == mark and board[3] == mark) or  #3rd column
    (board[7] == mark and board[5] == mark and board[3] == mark) or  #diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))   #diagonal

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Enter your position:(1-9) '))
    return position

def replay():
    choice = input('Do you want to play again ? ( y or n )')
    
print('WELCOME TO GAME : TIC TAC TOE!')

while True:
    game_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn =choose_first()
    print( turn + ' will start the game!')
    
    play_game = input('Ready to play the game?(y or n)')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            
            print_board(game_board)
            print("Player 1's turn ")
            position = player_choice(game_board)
            place_marker(game_board,player1_marker,position)
            
            if win_check(game_board,player1_marker):
                print_board(game_board)
                print('Congrats Player 1 you won the game!!!')
                game_on = False
            
            else:
                if full_board_check(game_board):
                    print_board(game_board)
                    print('Draw Game!')
                    game_on = False
                else:
                    turn = 'Player 2'
                    
        else:
            
            print_board(game_board)
            print("Player 2's turn ")
            position = player_choice(game_board)
            place_marker(game_board,player2_marker,position)
            
            if win_check(game_board,player2_marker):
                print_board(game_board)
                print('Congrats Player 2 you won the game!!!')
                game_on = False
            else:
                if full_board_check(game_board):
                    print_board(game_board)
                    print('Draw Game')
                    game_on = False
                
                else:
                    turn = 'Player 1'
                      
    if not replay():
            break