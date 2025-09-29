ROWS = 6
COLS = 7
COLUMN_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def resetBoard():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def printBoard(board):
    print()
    for row in reversed(range(ROWS)):
        print(f"| {row + 1} | " + " | ".join(board[row]) + " |")
    print("|R/C| " + " | ".join(COLUMN_LETTERS) + " |")
    print()

def checkLowest(board, col, row):
    # Check if this row is the lowest available one in the column
    for r in range(ROWS):
        if board[r][col] == " ":
            return r == row  
    return False  # Column is full

def getAvailablePositions(board):
    positions = []
    for col in range(COLS):
        for row in range(ROWS):
            if board[row][col] == " " and checkLowest(board, col, row):
                positions.append(f"{COLUMN_LETTERS[col]}{row + 1}")
                break
    return positions

def validateEntry(move, available_positions):
    if move in available_positions:
        return True
    else:
        print("Invalid move: that position is not available.")
        return False

def placeToken(board, col_letter, turn):
    col = COLUMN_LETTERS.index(col_letter)
    for row in range(ROWS):
        if board[row][col] == " ":
            board[row][col] = turn
            return row, col

def checkWin(board, turn):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == turn for i in range(4)):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == turn for i in range(4)):
                return True

    # Check diagonal /
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == turn for i in range(4)):
                return True

    # Check diagonal \
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == turn for i in range(4)):
                return True

    return False

def checkFull(board):
    return all(board[ROWS - 1][col] != " " for col in range(COLS))

def checkEnd(board, turn):
    if checkWin(board, turn):
        print(f"{turn} IS THE WINNER!!!")
        printBoard(board)
        return True
    elif checkFull(board):
        print("DRAW! NOBODY WINS!")
        printBoard(board)
        return True
    return False

def getMove(board):
    while True:
        available_positions = getAvailablePositions(board)
        print("Available positions are:", available_positions)
        move = input("Please enter column-letter and row-number (e.g., a1): ").strip().lower()

        if move == "reset":
            return 'reset'

        if validateEntry(move, available_positions):
            print("Thank you for your selection.")
            return move

def playGame():
    board = resetBoard()
    turn = "X"

    print("Welcome to Connect Four!")
    while True:
        if board == resetBoard():
            print("New game: X goes first.")
        printBoard(board)
        print(f"{turn}'s turn.")
        print(f"Where do you want your {turn} placed?")

        move = getMove(board)

        if move == 'reset':
            print("Game has been reset.")
            board = resetBoard()
            turn = "X"
            continue

        col_letter = move[0]
        row_index, col_index = placeToken(board, col_letter, turn)

        if checkEnd(board, turn):
            again = input("Another game (y/n)? ").strip().lower()
            if again == 'y':
                board = resetBoard()
                turn = "X"
            else:
                print("Thank you for playing!")
                break
        else:
            turn = "O" if turn == "X" else "X"

# Run the game
if __name__ == "__main__":
    playGame()
