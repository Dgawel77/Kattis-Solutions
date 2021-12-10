n = int(input())
nodes = {}
for x in range(n):
    x, y = map(int, input().split())
    nodes[x] = (x, y)
wires = {}
m = int(input())
for x in range(m):
    i, j = map(int, input().split())
    if i not in wires:
        wires[i] = set()
    wires[i].add(j)
    
    if j not in wires:
        wires[j] = set()
    wires[j].add(i)

l = int(input())
for _ in range(l):
    A, B = map(int, input().split())
    
print("")
