def printBoard(board):
    print(".................")
    print("|R\\C| 0 | 1 | 2 |")
    print("-----------------")
    i = 0
    for row in board:
        print(f"| {i}", end=" | ")
        print(" | ".join(row), end=" |\n")
        print("-----------------")
        i +=1
    print("")


def resetBoard():
    return [[" " for _ in range(3)] for _ in range(3)]


def validateEntry(row, col, board):
    if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] == " ":
            return True
        else:
            print("That cell is already taken.")
            print("Please make another selection.")
            return False
    else:
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1, or 2.")
        return False


def checkFull(board):
    for row in board:
        if " " in row:
            return False
    return True


def checkWin(board, turn):
    # Check rows
    for row in range(3):
        if all(board[row][col] == turn for col in range(3)):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == turn for row in range(3)):
            return True

    # Check diagonals
    if all(board[spot][spot] == turn for spot in range(3)) or all(board[spot][2 - spot] == turn for spot in range(3)):
        return True

    return False


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


def getMove():
    while True:
        move = input("Please enter row number and column number seperated by a comma. \n")
        if move.lower() == 'reset':
            return 'reset', 'reset'

        coords_str = move.split(",")
        if len(coords_str) != 2:
            print("Invalid input format. Please enter row and column as 'row,col' (e.g., 0,1).")
            continue

        row_str, col_str = coords_str[0], coords_str[1]

        if not (row_str.isdigit() and col_str.isdigit()):
            print("Invalid input: row and column must be numbers.")
            continue

        row, col = int(row_str), int(col_str)

        print(f"You have entered row #{row}")
        print(f"\t  and column #{col}")
        return row, col

def playGame():
    board = resetBoard()
    turn = "X"

    while True:
        if board == resetBoard(): 
            print("\nNew Game: X goes first.")
        printBoard(board)
        print(f"{turn}'s turn.")
        print(f"Where do you want your {turn} placed?")
        row, col = getMove()

        if row == 'reset':
            print("Game has been reset.")
            board = resetBoard()
            turn = "X"
            continue

        if validateEntry(row, col, board):
            print("Thank you for your selection.")
            board[row][col] = turn

            if checkEnd(board, turn):
                again = input("Play again? (y/n): ").lower()
                if again == 'y':
                    board = resetBoard()
                    turn = "X"
                else:
                    print("Thank you for playing!")
                    break
            else:
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"



# Run the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    playGame()
