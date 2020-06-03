def frame():
    print("---------")


def winner(who):
    return f"{who} wins"


def is_three_row(board, p):
    symbol = " " + p
    count_col = 0
    count_diag1 = 0
    count_diag2 = 0
    row_decrease = len(board) - 1
    for row in range(len(board)):
        if board[row].count(symbol) == 3:
            return True, winner(symbol)  # Player won by a row
        if board[row][row] == symbol:
            count_diag1 += 1
            if count_diag1 == 3:
                return True, winner(symbol)  # Player won by a diagonal \
        if board[row_decrease][row_decrease] == symbol:
            count_diag2 += 1
            if count_diag2 == 3:
                return True, winner(symbol)  # Player won by a diagonal /
        for col in range(len(board[row])):
            if board[col][row] == symbol:
                count_col += 1
                if count_col == 3:
                    return True, winner(symbol)  # Player won by a column
        row_decrease -= 1
        count_col = 0
        count_diag1 = 0
        count_diag2 = 0
    return False, ""


cell = str(input("Enter cells: "))
cell = [" "+i for i in cell]  # A list with one "front space" with a "number"
cell = [cell[i:i+3] for i in range(0, len(cell), 3)]  # A 3 number in a list within a list

frame()
for x in range(0, len(cell)):
    print(f"|{''.join(cell[x])} |")
frame()

print(cell)
print(is_three_row(cell, "x")[1])
print(is_three_row(cell, "o")[0])
