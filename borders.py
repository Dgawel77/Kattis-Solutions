def bfs(br, bc):
    global mark, region, n, m, count, BlackRegions, WhiteRegions
    stack = [(br, bc)]
    pos = 0
    parity = table[br][bc]
    if parity == '1':
        WhiteRegions.append(count)
    else:
        BlackRegions.append(count)
    while pos < len(stack):
        r, c = stack[pos]
        mark.add((r, c))
        region[(r, c)] = count
        moves = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for (nr, nc) in moves:
            if 0 <= nr < n and 0 <= nc < m:
                if table[nr][nc] == parity and (nr, nc) not in mark:
                    stack.append((nr, nc))
        pos += 1
    count += 1

#get data
n, m = map(int, input().split())
table = []
for r in range(n):
    table.append(input())

#make regions
region = {}
mark = set()
count = 1
BlackRegions = []
WhiteRegions = []
for r in range(n):
    for c in range(m):
        if (r, c) not in mark:
            bfs(r, c)

#link regions together
graph = {}
# for r in range(n):
#     for c in range(m):
        
print(BlackRegions)
print(WhiteRegions)
print(region)