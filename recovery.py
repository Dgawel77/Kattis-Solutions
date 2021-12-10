rowParity = list(map(int, list(input())))
columnParity = list(map(int, list(input())))
if rowParity.count(1) != columnParity.count(1):
    print(-1)
else:
    table = [[1 for _ in columnParity] for _ in rowParity]
    numberOfOnes = 0
    if (len(rowParity)-1) % 2 == 0:
        for i in range(1, len(columnParity)):
            if columnParity[i] == 1:
                table[0][i] = 1
                numberOfOnes += 1
            else:
                table[0][i] = 0
    else:
        for i in range(1, len(columnParity)):
            if columnParity[i] == 1:
                table[0][i] = 0
            else:
                table[0][i] = 1
                numberOfOnes += 1
    
    #print(numberOfOnes)
    if numberOfOnes % 2 == 0:
        if rowParity[0] == 0:
            table[0][0] = 0
        else:
            table[0][0] = 1
    else:
        if rowParity[0] == 1:
            table[0][0] = 1
        else:
            table[0][0] = 0
    
    if (len(columnParity)-1) % 2 == 0:
        for i in range(1, len(rowParity)):
            if rowParity[i] == 1:
                table[i][0] = 1
            else:
                table[i][0] = 0
    else:
        for i in range(1, len(rowParity)):
            if rowParity[i] == 1:
                table[i][0] = 0
            else:
                table[i][0] = 1
    
    for c in range(len(columnParity)-1, 0, -1):
        for r in range(len(rowParity)-1, 0, -1):
            #print(r, c)
            #if r != 0 and c != 0:
            if table[0][c] == 0 and table[r][0] == 0:
                table[0][c] = 1
                table[r][0] = 1
                table[r][c] = 0
                table[0][0] = 1 if table[0][0] == 0 else 1
    
    for r in table:
        for c in r:
            print(c, end='')
        print()
        
#1111111001111111 65k
#1111011111101111 63471
