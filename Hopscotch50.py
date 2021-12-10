curmin = 30000000
def dofor(i):
    global curmin
    for r1, c1 in d[i]:
        if i == 1:
            distance[r1][c1] = 0
        for r2, c2 in d[i+1]:
            curdist = distance[r1][c1] + manhattan(r1, c1, r2, c2)
            distance[r2][c2] = min(curdist, distance[r2][c2])
            if i+1 == k:
                curmin = min(curmin, curdist)


def manhattan(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


n, k = map(int, input().split())
d = {}
distance = []
nums = set()
for i in range(1, k+1):
    d[i] = []
for r in range(n):
    for c, i in enumerate(list(map(int, input().split()))):
        d[i].append((r, c))
        nums.add(i)
    distance.append([30000000 for _ in range(n)])


if set(range(1, k+1)) == nums:
    ran = False
    for i in range(1, k):
        dofor(i)
        ran = True
    print(curmin if ran else 0)
else:
    print(-1)
