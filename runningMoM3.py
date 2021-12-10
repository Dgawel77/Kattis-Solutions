def dfs(v):
    global mark
    mark.add(v)
    for c in g[v]:
        if c in mark:
            return True
        mark.add(c)
        if dfs(c):
            return True
        mark.remove(c)
    return False

n = int(input())
g = {}
for _ in range(n):
    line = input().split()
    for d in line:
        if d not in g:
            g[d] = []
    g[line[0]].append(line[1])
    
while True:
    try:
        city = input()
        mark = set()
        print(city, ['trapped', 'safe'][dfs(city)])
    except EOFError:
        break