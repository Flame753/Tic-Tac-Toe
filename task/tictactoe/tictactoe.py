def frame():
    print("---------")


def reset(task):
    task = 0
    return task


def is_three_row(board, p):
    symbol = " " + p
    count = 0
    for row in range(len(board)):
        if board[row].count(symbol) == 3:
            pass  # Player won
        for col in range(len(board[row])):
            if board[col][row] == symbol:
                count += 1
                if count == 3:
                    pass  # Player won
        reset()


cell = str(input("Enter cells: "))
cell = [" "+i for i in cell]  # A list with one "front space" with a "number"
cell = [cell[i:i+3] for i in range(0, len(cell), 3)]  # A 3 number in a list within a list

frame()
for x in range(0, len(cell)):
    print(f"|{''.join(cell[x])} |")
frame()

print(cell)
is_three_row(cell, "x", "o")
