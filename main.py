import sys

from rich_menu import Menu


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
        if all(board[i][j] == symbol for j in range(3)) or all(
            board[j][i] == symbol for j in range(3)
        ):
            return True

    if all(board[i][i] == symbol for i in range(3)) or all(
        board[i][2 - i] == symbol for i in range(3)
    ):
        return True
    return False


def convert_input_to_coordinates(input_str):
    line, column_str = input_str[:-1], input_str[-1].upper()
    line = int(line) - 1
    column = ord(column_str) - ord("A")
    return line, column


def get_input(board):
    input_str = input("type the number for the line and the column (e.g., 2A): ")
    while True:
        try:
            line, column = convert_input_to_coordinates(input_str)

            if not (0 <= line < 3 and 0 <= column < 3 and board[line][column] == " "):
                input_str = input(
                    "this position is already taken or the input is out of bounds. please enter a valid coordinate (e.g., 2A): "
                )
                continue
            print()  # enter a new line
            return line, column
        except ValueError:
            input_str = input(
                "invalid input. please enter a valid coordinate (e.g., 2A): "
            )
        except KeyboardInterrupt:
            sys.exit()


def new_board(turn: callable, board, player_1, player_2, letters):
    move = 0
    while True:
        print_board(board, letters)
        print(
            f"\nPlayer 1 ({player_1}):" if not move % 2 else f"\nPlayer 2 ({player_2}):"
        )

        line, column = get_input(board)

        board[line][column] = turn(player_1, player_2, move)
        move += 1

        if check_winner(board, turn(player_1, player_2, move - 1)):
            print_board(board, letters)
            print(f"\nplayer {turn(player_1, player_2, move - 1)} won!\n")
            break

        if move == 9:
            print_board(board, letters)
            print("\nit's a draw!\n")
            break


def game():
    board, letters = create_board()
    player_1, player_2 = choose_icon()
    new_board(turn, board, player_1, player_2, letters)
    response = input("do you want to play a new game? [y/N] ")
    if response.lower() == "y":
        game()
    else:
        print("exiting game...")
        sys.exit()


def main():
    game()


if __name__ == "__main__":
    main()
