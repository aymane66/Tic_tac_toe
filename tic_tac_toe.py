# Welcome message
print("Welcome to Tic Tac Toe")

# Get player names
name_X = input("X Player name: ")
name_O = input("O Player name: ")
print(f"Welcome {name_X} and {name_O}. Let's play!")

# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print(" | ".join(map(str, row)))
        print("-" * 9)

# Function to update the board with a player's move
def update_board(board, move, player):
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = player

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Initialize the game board
game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Set the current player to 'X'
current_player = 'X'

# Main game loop
print("Insert the number of the square you choose")
while True:
    # Display the current state of the board
    display_board(game_board)
    
    try:
        # Get the next move from the current player
        move = int(input(f"{name_X if current_player == 'X' else name_O}'s move: "))
        
        # Validate the move
        if 1 <= move <= 9 and game_board[(move - 1) // 3][(move - 1) % 3] == 0:
            # Update the board with the move
            update_board(game_board, move, current_player)
            
            # Check for a winner
            if check_winner(game_board, current_player):
                display_board(game_board)
                print(f"{name_X if current_player == 'X' else name_O} wins!")
                break

            # Check for a draw
            if all(cell != 0 for row in game_board for cell in row):
                display_board(game_board)
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Please choose an empty square (1-9).")
    except ValueError:
        print("Invalid input. Please enter a number.")
