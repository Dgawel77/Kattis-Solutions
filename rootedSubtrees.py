import math
#lca code
def dfs(u, p, memo, lev, log, g):
    memo[u][0] = p
    for i in range(1, log + 1):
        memo[u][i] = memo[memo[u][i - 1]][i - 1]

    for v in g[u]:
        if v != p:
            lev[v] = lev[u] + 1
            dfs(v, u, memo, lev, log, g)


def lca(u, v, log, lev, memo):
    if lev[u] < lev[v]:
        swap(u, v)

    for i in range(log, -1, -1):
        if (lev[u] - pow(2, i)) >= lev[v]:
            u = memo[u][i]

    if u == v:
        return v

    for i in range(log, -1, -1):
        if memo[u][i] != memo[v][i]:
            u = memo[u][i]
            v = memo[v][i]

    return memo[u][0]


n, q = map(int, input().split())

g = [[] for i in range(n + 1)]

log = math.ceil(math.log(n, 2))
memo = [[-1 for i in range(log + 1)] 
            for j in range(n + 1)]

lev = [0 for i in range(n + 1)]

g[1].append(2)
g[2].append(1)
g[1].append(3)
g[3].append(1)
g[1].append(4)
g[4].append(1)
g[2].append(5)
g[5].append(2)
g[3].append(6)
g[6].append(3)
g[3].append(7)
g[7].append(3)
g[3].append(8)
g[8].append(3)
g[4].append(9)
g[9].append(4)

dfs(1, 1, memo, lev, log, g)

print("The LCA of 6 and 9 is", lca(6, 9, log, lev, memo))
