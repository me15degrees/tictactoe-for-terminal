from rich_menu import Menu
import time
import sys

def create_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    letters = ["A", "B", "C"]
    return board, letters

def print_board(board, letters):
    print("   " + "   ".join(letters))
    for i, line in enumerate(board):
        print(f"{i+1}  " + " | ".join(line))
        if i != 2:
            print("  ---|---|---")

menu = Menu(
    "X",
    "O",
    color="green",
    rule_title="tic tac toe",
    align="center",
    panel_title="choose your icon",
    selection_char="*",
)
selected = menu.ask(screen=False)

def choose_icon():
    player_1 = selected
    if selected == "O":
        player_2 = "X"
    else:
        player_2 = "O"
    return player_1, player_2

def turn(player_1, player_2, move):
    return player_1 if move % 2 == 0 else player_2

def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def convert_input_to_coordinates(input_str):
    line, column_str = input_str[:-1], input_str[-1].upper()
    line = int(line) - 1
    column = ord(column_str) - ord('A')
    return line, column

def new_board(turn, board, player_1, player_2,letters):
    move = 0
    while True:
        print_board(board, letters)
        input_str = input("type the number for the line and the column (e.g., 2A): ")
        
        try:
            line, column = convert_input_to_coordinates(input_str)
        except ValueError:
            print("invalid input. please enter a valid coordinate (e.g., 2A).")
            continue

        if 0 <= line < 3 and 0 <= column < 3 and board[line][column] == " ":
            board[line][column] = turn(player_1, player_2, move)
            move += 1
        else:
            print("this position is already taken or the input is out of bounds. try again.")
            continue

        if check_winner(board, turn(player_1, player_2, move - 1)):
            print_board(board, letters)
            print(f"player {turn(player_1, player_2, move - 1)} won!")
            break

        if move == 9:
            print_board(board, letters)
            print("it's a draw!")
            break
def game():
    board, letters = create_board()
    player_1, player_2 = choose_icon()
    new_board(turn, board, player_1, player_2,letters)
    response = input("do you want to play a new game? y/n ")
    if response.lower() == "y":
        game()
    else:
        time.sleep(1)
        print("exiting game...")
        time.sleep(1)
        sys.exit(1)

def main():
    game()

if __name__ == "__main__":
    main()