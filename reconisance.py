def eq(t):
    global pairs
    low = 1000000000000000000
    high = -1000000000000000000
    for x, v in pairs:
        calc = x + (v * t)
        low = min(calc, low)
        high = max(calc, high)
    return high - low

def tSearch(l, r):
    if r < 0 or l > r:
        return
    a = l + ((r-l)/3)
    b = r - ((r-l)/3)
    eqA, eqB = eq(a), eq(b)
    if abs(eqA - eqB) < 0.00001:
        print(eqA)
    else:
        if eqA > eqB:
            tSearch(a, r)
        elif eqA == eqB:
            tSearch(a, b)
        elif eqA < eqB:
            tSearch(l, b)
    return

n = int(input())
pairs = []
for _ in range(n):
    x, v = map(int, input().split())
    pairs.append((x, v))

tSearch(0, 200_000)