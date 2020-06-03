# write your code here
def frame():
    print("---------")


def is_three_row(state):
    if x in state:
        print("yes")


cell = str(input("Enter cells: "))
cell = [" "+i for i in cell]  # A list with one "front space" with a "number"
cell = [cell[i:i+3] for i in range(0, len(cell), 3)]  # A 3 number in a list within a list

frame()
for x in range(0, len(cell)):
    print(f"|{''.join(cell[x])} |")
frame()

print(cell)
is_three_row(cell)