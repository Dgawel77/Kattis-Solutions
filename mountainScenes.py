MOD = 1000000007
def f(w, ribbon):
    global table
    if ribbon < 0:
        return 0
    if w > W:
        return 1
    if table[w][ribbon] != None:
        return table[w][ribbon]
    scenes = 0
    for x in range(H+1):
        scenes = scenes + f(w+1, ribbon-x)
    table[w][ribbon] = scenes % MOD
    return table[w][ribbon]

N, W, H = map(int, input().split())
table = [[None for _ in range(N+1)] for _ in range(W+1)]

ribbon_sqaures = min(W * H, N)
plains = (ribbon_sqaures // W) + 1
print(((f(1, N) - plains)+MOD) % MOD)
for row in table:
    print(row)
