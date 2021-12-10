def DFS(s, route):
    global found, mark
    if found:
        return
    route.append(s)
    mark.add(s)
    if s == end:
        out = ""
        for r in route:
            out += r + " "
        print(out)
        route.pop()
        found = True
        return
    for connection in graph[s]:
        if connection not in mark:
            DFS(connection, route)
    route.pop()


R = int(input())
graph = {}
v = set()
for _ in range(0, R):
    line = input().split()
    for member in line:
        if member not in v:
            graph[member] = set()
            v.add(member)
    for goTo in line[1:]:
        graph[line[0]].add(goTo)
        graph[goTo].add(line[0])

start, end = input().split()
mark = set()
found = False
if start in v:
    DFS(start, [])
if not found:
    print("no route found")