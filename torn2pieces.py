def dfs(v):
    global G,p,end,mark
    mark.add(v)
    for w in G[v]:
        if w not in mark:
            p[w] = v
            if w==end:
                return -1
            res = dfs(w)
            if res == -1:
                return -1
    return 0

def prnt(ending):
    global start
    if ending != start:
        prnt(p[ending])
        print(" " + ending, end='')

N = int(input())
G,p = {},{}
V = set()

for j in range(N):
    line = input().split()
    s1 = line[0]
    if s1 not in V:
        V.add(s1)
        G[s1] = set()
    for i in range(1, len(line)):
        si = line[i]
        G[s1].add(si)
        if si not in V:
            V.add(si)
            G[si] = set()
        G[si].add(s1)


start, end = input().split()
mark = set()
p[start]=''
if start not in V:
    r = 0
else:
    r = dfs(start)

if r == 0:
    print("no route found")
else:
    print(start, end="")
    prnt(end)




