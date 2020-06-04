def frame():
    print("---------")


def winner(who):
    return f"{who} wins"


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
            return True, winner(symbol)  # Player won by a row
        if board[row][row] == symbol:
            backslash_counter += 1
            if backslash_counter == 3:
                return True, winner(symbol)  # Player won by a backslash \
        if board[row][slash] == symbol:
            slash_counter += 1
            if slash_counter == 3:
                return True, winner(symbol)  # Player won by a diagonal /
        for col in range(len(board[row])):
            if board[col][row] == symbol:
                col_counter += 1
                if col_counter == 3:
                    return True, winner(symbol)  # Player won by a column
        slash -= 1
        col_counter = 0
    return False, f"{symbol} lost"


cell = str(input("Enter cells: ")).upper()
cell = [" "+i for i in cell]  # A list with one "front space" with a "number"
cell = [cell[i:i+3] for i in range(0, len(cell), 3)]  # A 3 number in a list within a list

frame()
for x in range(0, len(cell)):
    print(f"|{''.join(cell[x])} |")
frame()

if is_three_row(cell, "X")[0] and is_three_row(cell, "O")[0] or abs(many(cell, "X") - many(cell, "O")) >= 2:
    print("Impossible")
elif not is_three_row(cell, "X")[0] and not is_three_row(cell, "O")[0] and many(cell, "X") + many(cell, "O") != 9:
    print("Game not finished")
elif not is_three_row(cell, "X")[0] and not is_three_row(cell, "O")[0] and many(cell, "X") + many(cell, "O") == 9:
    print("Draw")
elif is_three_row(cell, "X")[0]:
    print(winner("X"))
elif is_three_row(cell, "O")[0]:
    print(winner("O"))
else:
    print("There is a problem with the code!")