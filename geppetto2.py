total = 0
def solve(pizza, i):
    global n, total
    for ing in range(i, n+1):
        if len(pizza.intersection(rests[ing])) == 0:
            pizza.add(ing)
            total += 1
            solve(pizza, ing)
            pizza.remove(ing)
    return

n, m = map(int, input().split())
rests = {}
for x in range(1, n+1):
    rests[x] = set()
    rests[x].add(x)
for _ in range(0, m):
    a, b = map(int, input().split())
    rests[a].add(b)
    rests[b].add(a)
solve(set(), 1)
print(total+1)
    