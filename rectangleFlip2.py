n, m = map(int, input().split())
board = []
for r in range(n):
    board.append([])
    for c in range(m):
        board[r].append(False)

sufix = []
for r in range(n):
    sufix.append([])
    for c in range(m):
        sufix[r].append([0, m-1])

total = ((n * (n + 1))//2) * ((m * (m + 1))//2)
for _ in range(n * m):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    for c in range(j+1, m):
        sufix[i][c][0] = j + 1
        if board[i][c]:
            break
        
    for c in range(j-1, -1, -1):
        sufix[i][c][1] = j - 1
        if board[i][c]:
            break
    
    #print(i, j)
    #for r in sufix:
    #    print(r)
    
    count = 0
    uminL, uminR = 1000, 1000
    dminL, dminR = 1000, 1000
    for u in range(i, -1, -1):
        if not board[u][j]:
            uminL, uminR = min(uminL, j - sufix[u][j][0]), min(uminR, sufix[u][j][1] - j)
            for d in range(i, n):
                if not board[d][j]:
                    dminL, dminR = min(dminL, j - sufix[d][j][0]), min(dminR, sufix[d][j][1] - j)
                    count += (min(uminL, dminL) + 1) * (min(uminR, dminR) + 1)
                else:
                    break
            #minL, minR = j - sufix[u][j][0], j - sufix[u][j][1]            
        else:
            break

    total -= count
    print(total)
    #print()
    board[i][j] = True