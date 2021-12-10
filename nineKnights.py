def click(row, col):
    global rows
    possible = [(col+1, row+2), (col-1, row+2), (col+2, row-1), (col+2, row+1),
                (col+1, row-2), (col-1, row-2), (col-2, row+1), (col-2, row-1)]
    for pos in possible:
        if (0 <= pos[0] <= 4) and (0 <= pos[1] <= 4):
            if rows[pos[1]][pos[0]] == "k":
                return False
    return True


rows = []
for _ in range(0, 5):
    rows.append(input())
breakOut = False
kings = 0
for row in enumerate(rows):
    if breakOut:
        break
    else:
        for letter in enumerate(row[1]):
            if letter[1] == "k":
                kings += 1
                if not click(row[0], letter[0]):
                    print("invalid")
                    breakOut = True
                    break
if not breakOut:
    if kings != 9:
        print("invalid")
    else:
        print("valid")
