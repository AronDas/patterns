rows = int(input("Please enter the number of rows here"))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for a in range(i):
        print("*", end=" ")
    print()
