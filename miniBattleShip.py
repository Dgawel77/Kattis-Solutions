def simulation(m):
    global table, grid, n, k, ships, Ocount
    if m >= k:
        if Ocount == 0:
            return 1
        return 0
    l = ships[m]
    ans = 0
    for r in range(n):
        for c in range(n):
            if table[r][c] != 'X':
                # down
                if r + l <= n:
                    suc = True
                    for nr in range(r, r + l):
                        if table[nr][c] == 'X' or grid[nr][c]:
                            suc = False
                            break
                    if suc:
                        OinThis = 0
                        for nr in range(r, r + l):
                            grid[nr][c] = True
                            if table[nr][c] == 'O':
                                Ocount -= 1
                                OinThis += 1
                        ans += simulation(m+1)
                        for nr in range(r, r + l):
                            grid[nr][c] = False
                        Ocount += OinThis
                # left
                if c + l <= n and l != 1:
                    suc = True
                    for nc in range(c, c + l):
                        if table[r][nc] == 'X' or grid[r][nc]:
                            suc = False
                            break
                    if suc:
                        OinThis = 0
                        for nc in range(c, c + l):
                            grid[r][nc] = True
                            if table[r][nc] == 'O':
                                Ocount -= 1
                                OinThis += 1
                        ans += simulation(m+1)
                        for nc in range(c, c + l):
                            grid[r][nc] = False
                        Ocount += OinThis
    return ans


n, k = map(int, input().split())
Ocount = 0
table = []
grid = []
for _ in range(n):
    line = input()
    table.append(line)
    for c in line:
        if c == 'O':
            Ocount += 1
    grid.append([False for _ in range(0, n)])

ships = []
for _ in range(k):
    ships.append(int(input()))
print(simulation(0))