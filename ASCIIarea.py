h, w = map(int, input().split())
area = 0
inside = False
for _ in range(h):
    line = input()
    for c in line:
        if c == '\\' or c == '/':
            area += .5
            inside = not inside
        if c == '.' and inside:
            area += 1
print(int(area))