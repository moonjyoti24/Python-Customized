from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def print_board(board):
print("\n")
for row in board:
print(" | ".join(row))
print("-" * 5)

# Function to check for a winner
def check_winner(board, player):
# Check rows, columns, and diagonals
for row in board:
if all(cell == player for cell in row):
return True
for col in range(3):
if all(row[col] == player for row in board):
return True
if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
return True
return False

# Main game function
def tic_tac_toe():
board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
turn = 0

while turn < 9:
print_board(board)
current_player = players[turn % 2]
print(f"Player {current_player}'s turn.")

try:
row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
if board[row][col] != " ":
print("Cell already taken! Try again.")
continue
board[row][col] = current_player
if check_winner(board, current_player):
print_board(board)
print(f"Player {current_player} wins!")
return
turn += 1
except (ValueError, IndexError):
print("Invalid input! Enter numbers between 0 and 2.")

print_board(board)
print("It's a draw!")

# Run the game
tic_tac_toe()

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')


