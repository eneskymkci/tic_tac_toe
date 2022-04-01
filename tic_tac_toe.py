from IPython.display import clear_output

def display_board(board):
    
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
    
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def tic_tac_toe():
    
    print('Welcome to Tic Tac Toe!')
    
    player1 = input('Do yo want to be X or O?')
    clear_output()
    
    if player1 == 'X':
        
        player2 = 'O'
        
    elif player1 == 'O':
        
        player2 = 'X'
    
    win = False
       
    ready = input('Are you ready to play? Enter Yes or No: ')
    clear_output()
    


    while ready == 'Yes' and win == False:
        
        display_board(board)
            
        position = int(input('Player 1 choose your next position (1-9): '))
        clear_output()
            
        board[position] = player1  
        
        if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X' or
            board[1] == 'O' and board[2] == 'O' and board[3] == 'O' or
            board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or
            board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or
            board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or
            board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or
            board[4] == 'X' and board[5] == 'X' and board[6] == 'X' or
            board[4] == 'O' and board[5] == 'O' and board[6] == 'O' or
            board[7] == 'X' and board[8] == 'X' and board[9] == 'X' or
            board[7] == 'O' and board[8] == 'O' and board[9] == 'O' or
            board[1] == 'X' and board[5] == 'X' and board[9] == 'X' or
            board[1] == 'O' and board[5] == 'O' and board[9] == 'O' or
            board[3] == 'X' and board[5] == 'X' and board[7] == 'X' or
            board[3] == 'X' and board[6] == 'X' and board[9] == 'X' or
            board[3] == 'O' and board[6] == 'O' and board[9] == 'O' or
            board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
            
            win = True
            print("Congratulations! You've won the game!")
            break 

        display_board(board)
            
        position = int(input('Player 2 choose your next position (1-9): '))
        clear_output()
        
        board[position] = player2

        if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X' or
            board[1] == 'O' and board[2] == 'O' and board[3] == 'O' or
            board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or
            board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or
            board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or
            board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or
            board[4] == 'X' and board[5] == 'X' and board[6] == 'X' or
            board[4] == 'O' and board[5] == 'O' and board[6] == 'O' or
            board[7] == 'X' and board[8] == 'X' and board[9] == 'X' or
            board[7] == 'O' and board[8] == 'O' and board[9] == 'O' or
            board[1] == 'X' and board[5] == 'X' and board[9] == 'X' or
            board[1] == 'O' and board[5] == 'O' and board[9] == 'O' or
            board[3] == 'X' and board[5] == 'X' and board[7] == 'X' or
            board[3] == 'X' and board[6] == 'X' and board[9] == 'X' or
            board[3] == 'O' and board[6] == 'O' and board[9] == 'O' or
            board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
            
            win = True
            print("Congratulations! You've won the game!")
            break 
            
    else:
            
        print('Exit')
