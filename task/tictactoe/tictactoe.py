# write your code here
def frame():
    print("---------")


cell = str(input("Enter cells: "))
cell = [" "+i for i in cell]  # List with one "front space" with a "number"
cell = [cell[i:i+3] for i in range(0, len(cell), 3)]  # 3 values in a list within a list

frame()
for x in range(0, len(cell)):
    print(f"|{''.join(cell[x])} |")
frame()
