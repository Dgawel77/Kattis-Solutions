def solve(i, t):
    global m
    if i >= n:
        return
    if t - m[i] >= 0:
        if (table[t][i-1][1]) < (table[t - m[i]][i][1]):
            table[t - m[i]][i] = (table[t][i-1][0] << 1, table[t][i-1][1])
            solve(i+1, t-m[i])
    if (table[t][i-1][1]) < (table[t + m[i]][i][1]):
        table[t + m[i]][i] = ((table[t][i-1][0] << 1) | 1, t + m[i] if t + m[i] > table[t][i-1][1] else  table[t][i-1][1])
        solve(i+1, t+m[i])

p = int(input())
for _ in range(0, p):
    n = int(input())
    m = list(map(int, input().split()))
    
    table = [[(0, 9999) for _ in range(0, n)] for _ in range(0, 1001)]
    table[m[0]][0] = (1, m[0])
    solve(1, m[0])
    #for row in enumerate(table[:80]):
    #    print(row[0], row[1])
    if table[0][n-1] ==(0, 9999):
        print("IMPOSSIBLE")
    else:
        output = ""
        for bit in str(bin(table[0][n-1][0]))[2:]:
            if bit == "1":
                output += "U"
            if bit == "0":
                output += "D"
        print(output)