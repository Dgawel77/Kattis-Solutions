def index(c):
    pos = ord(c) - 65
    if c == '_':
        pos = 26
    return pos

def solve(v, start):
    goTo[start].append(v)
    if map[index(v)] not in goTo[start]:
        solve(map[index(v)], start)
 
goTo =[]
map = []
for _ in range(27):
    map.append(input())
    goTo.append([])

for pos, c in enumerate(map):
    solve(c, pos)

rep = int(input())
line = input()
out = ''
for c in line:
    char = (rep % len(goTo[index(c)])) - 1
    out += goTo[index(c)][char]

# for r in goTo:
#     print(r)
    
print(out)