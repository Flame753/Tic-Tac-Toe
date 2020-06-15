import string


def frame():
    print(9 * "-")


def many(board, p):
    symbol = " " + p
    total = 0
    for row in range(len(board)):
        amount = board[row].count(symbol)
        total += amount
    return total


def is_three_row(board, p):
    symbol = " " + p
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
    if coord == [1, 1]:
        return [2, 0]
    elif coord == [1, 2]:
        return [1, 0]
    elif coord == [1, 3]:
        return [1, 3]
    elif coord == [2, 1]:
        return coord
    elif coord == [2, 2]:
        return [1, 1]
    elif coord == [2, 3]:
        return [0, 1]
    elif coord == [3, 1]:
        return [2, 2]
    elif coord == [3, 2]:
        return [1, 2]
    elif coord == [3, 3]:
        return [0, 2]
    return coord


# Returns True if the spot is empty
def is_empty(board, coord):
    if_piece_there = board[coord[0]][coord[1]]
    if if_piece_there in ["X", "O"]:
        return False
    else:
        return True


cell = str(input("Enter cells: ")).upper()
cell = [" " + i for i in cell]  # A list with one "front space" with a "number"
cell = [cell[i:i + 3] for i in range(0, len(cell), 3)]  # A 3 number in a list within a list

frame()
for x in range(0, len(cell)):
    print(f"|{''.join(cell[x])} |")
frame()

valid = False
while not valid:
    coordinate = [x for x in input("Enter the coordinates: ")]
    coordinate.remove(" ")
    coordinate = [int(x) for x in coordinate]  # Exception here
    if type(coordinate) == str():  # Need some more work (Look into Exceptions)
        print("You should enter numbers!")
    if coordinate not in [[x, y] for x in range(1, 4) for y in range(1, 4)]:  # Good
        print("Coordinates should be from 1 to 3!")
    if is_empty(cell, coord_convert(coordinate)):
        print("works")  # Need to finish; put x or o in that spot
    else:
        print("This cell is occupied! Choose another one!")
    break

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
