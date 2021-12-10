def solve(city):
    global mark, checkCity, found
    if found:
        return
    mark.add(city)
    for c in graph[city]:
        if c == checkCity:
            found = True
            return
        if c not in mark:
            solve(c)
    return

R = int(input())
mark = set()
found = False
graph = {}
v = set()
for _ in range(0, R):
    line = input().split()
    for city in line:
        if city not in v:
            graph[city] = set()
            v.add(city)
    graph[line[0]].add(line[1])

while True:
    try:
        checkCity = input()
    except:
        break
    if checkCity == '' or checkCity not in v:
        break
    mark = set()
    found = False
    solve(checkCity)
    if found:
        print(checkCity + " safe")
    else:
        print(checkCity + " trapped")