import sys
def solve(i, Sa, Ba, total):
    if i >= R:
        if total > 0:
            return (Sa, Ba)
        else:
            return (sys.maxsize, 0)
    withIng = solve(i+1, Sa*ings[i][0], Ba+ings[i][1], total+1)
    withoutIng = solve(i+1, Sa, Ba, total)
    if abs(withIng[0]-withIng[1]) < abs(withoutIng[0]-withoutIng[1]):
        return withIng
    else:
        return withoutIng

R = int(input())
ings = []
for _ in range(0, R):
    S, B = map(int, input().split())
    ings.append((S, B))
soup = solve(0, 1, 0, 0)
print(abs(soup[0] - soup[1]))