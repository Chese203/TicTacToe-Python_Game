def display_board(board):
    # Accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    for row in board:
        print('|       |       |       |')
        for col in row:
            print('|  ',col,'  ',end='')
        print('|')
        print('|       |       |       |')
        print('+-------+-------+-------+')

def enter_move(board):
    # Accepts the board's current status, asks the user for their move, 
    # checks the input, and updates the board according to the user's decision.
    
    while True:  # Infinite loop to keep prompting until valid input
        # Input validation to ensure a correct number is given
        try: 
            move = int(input('Enter your move (1-9): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 9.')
            continue  # Restart the loop

        if move < 1 or move > 9:
            print('Invalid move. Please choose a number between 1 and 9.')
            continue  # Restart the loop

        for row in range(3):
            for col in range(3):
                if board[row][col] == move:  # Check if cell is free
                    board[row][col] = 'O'  # Update the board
                    return  # Exit the loop and function

        print('That square is already taken. Try again.')  # Prompt again

    
def make_list_of_free_fields(board):
    # Browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' and board[row][col] != 'O':
                free_fields.append((row,col))
        
    return free_fields
    
def victory_for(board, sign):
    # Analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    # Checks if a row is complete 
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True
    # Checks if a column is complete
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True
   # Checks top-left to bottom-right
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):  
        return True
    
    # Checks top-right to bottom-left
    if (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):  
        return True
    return False

def draw_move(board):
    # Draws the computer's move and updates the board.
    from random import randrange
    
    while True:
        move = randrange(1,10)
        
        for row in range(3):
            for col in range(3):
                if board[row][col] == move:
                    board[row][col] = 'X'
                    display_board(board)
                    return

# Main Function Run

# Initialize the board and victory variable
board =[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
victory = False

# Show the board at the start
display_board(board)

# Computer takes its designated first move
print('First, my move!')
board[1][1] = 'X'
display_board(board)

# Starts the loop to check who has won
while not victory:
    
    if not make_list_of_free_fields(board):
        print('Draw!')
        break
        
    if victory_for(board, 'O'):
        display_board(board)
        print('You win!')
        break 
    
    if victory_for(board,'X'):
        display_board(board)
        print('I win!')
        break 
    # Player is prompted for their first move. If valid, the board is updated and shown 
    enter_move(board)
    display_board(board)
    
# AFter the player move, checks for winners again 
    if not make_list_of_free_fields(board):
        print('Draw!')
        break
    
    if victory_for(board, 'O'):
        display_board(board)
        print('You win!')
        break 
    
    if victory_for(board,'X'):
        display_board(board)
        print('I win!')
        break 
    draw_move(board)
    


