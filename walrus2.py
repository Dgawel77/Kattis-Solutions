import sys
sys.setrecursionlimit(1100)
Onekfound = False
def solve(i, t):
    global Onekfound
    if Onekfound:
        return
    if i > n-1 or t > 1000:
        return
    if t == 1000:
        Onekfound = True
        return
    if not table[t][i]:
        table[t][i] = True
        solve(i+1, t)
    if not table[t+w[i]][i]:
        table[t+w[i]][i] = True
        solve(i+1, t+w[i])

n = int(input())
w = []
for _ in range(0, n):
    w.append(int(input()))
table = [[False for _ in range(0, n)] for _ in range(0, 2001)]
solve(0, 0)

for i in range(0, 1001):
    if True in table[1000+i]:
        print(1000+i)
        break
    elif True in table[1000-i]:
        print(1000-i)
        break