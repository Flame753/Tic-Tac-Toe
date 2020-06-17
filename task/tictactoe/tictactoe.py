def frame():
    print(9 * "-")


def print_board(board):
    frame()
    for x in range(0, len(board)):
        print(f"|{''.join(board[x])} |")
    frame()


def add_space(symbol):
    return " " + symbol


def many(board, p):
    symbol = add_space(p)
    total = 0
    for row in range(len(board)):
        amount = board[row].count(symbol)
        total += amount
    return total


def is_three_row(board, p):
    symbol = add_space(p)
    col_counter = 0
    backslash_counter = 0
    slash = - 1
    slash_counter = 0
    for row in range(len(board)):
        if board[row].count(symbol) == 3:
            return True  # Player won by a row
        if board[row][row] == symbol:
            backslash_counter += 1
            if backslash_counter == 3:
                return True  # Player won by a backslash \
        if board[row][slash] == symbol:
            slash_counter += 1
            if slash_counter == 3:
                return True  # Player won by a diagonal /
        for col in range(len(board[row])):
            if board[col][row] == symbol:
                col_counter += 1
                if col_counter == 3:
                    return True  # Player won by a column
        slash -= 1
        col_counter = 0
    return False


# Coordinates Converter; Argument: A list, Returns: New Converter
def coord_convert(coord):
    i = 3 - coord[1]
    j = coord[0] - 1
    return i, j


# Returns True if the spot is empty
def is_empty(board, coord):
    if_piece_there = board[coord[0]][coord[1]]
    symbols = [" X", " O"]
    if if_piece_there in symbols:
        return False
    else:
        return True


cell = " " * 9  # The Board
cell = [" " + i for i in cell]  # A list with one "front space" with a "number"
cell = [cell[i:i + 3] for i in range(0, len(cell), 3)]  # A 3 number in a list within a list
print_board(cell)

turn = 0
player = ["X", "O"]
while turn < 9 and not is_three_row(cell, "X") and not is_three_row(cell, "O"):  # Checks User input and shows field
    try:
        coordinate = input("Enter the coordinates: ")
        coordinate = (int(coordinate[0]), int(coordinate[2]))

        new_coord = coord_convert(coordinate)
        if coordinate not in [(x, y) for x in range(1, 4) for y in range(1, 4)]:
            print("Coordinates should be from 1 to 3!")
        elif is_empty(cell, new_coord):
            cell[new_coord[0]][new_coord[1]] = add_space(player[turn % 2])
            print_board(cell)
            turn += 1
        else:
            print("This cell is occupied! Choose another one!")
    except ValueError:
        print("You should enter numbers!")
    except IndexError:
        print("You should enter numbers!")


if is_three_row(cell, "X") and is_three_row(cell, "O") or abs(many(cell, "X") - many(cell, "O")) >= 2:
    print("Impossible")
elif not is_three_row(cell, "X") and not is_three_row(cell, "O") and many(cell, "X") + many(cell, "O") != 9:
    print("Game not finished")
elif not is_three_row(cell, "X") and not is_three_row(cell, "O") and many(cell, "X") + many(cell, "O") == 9:
    print("Draw")
elif is_three_row(cell, "X"):
    print("X wins")
elif is_three_row(cell, "O"):
    print("O wins")
else:
    print("There is a problem with the code!")
