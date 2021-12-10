import sys
n, m = map(int, input().split())
cities = {}
cityLen = {}
save = {}
citysave = {}
for _ in range(0, n):
    line = input()
    cities[line] = []
    save[line] = []
    cityLen[line] = [sys.maxsize, []]
    citysave[line] = [sys.maxsize, []]
for _ in range(0, m):
    line = input().split()
    cities[line[0]].append((line[1], int(line[2])))
    cities[line[1]].append((line[0], int(line[2])))
    save[line[0]].append((line[1], int(line[2])))
    save[line[1]].append((line[0], int(line[2])))
assignment = []
for _ in range(0, 4):
    assignment.append(input().split())

total = 0
paths = set()
for k in range(0, 4):
    total = 0
    for i in range(0, 4):
        start = assignment[(i+k)%4][0]
        end = assignment[(i+k)%4][1]
        cityLen[start] = [0, [start]]
        stack = [start]
        if start == end:
            stack = []
        x = 0
        while x < len(stack):
            u = stack[x]
            for e in cities[u]:
                if cityLen[u][0] + e[1] < cityLen[e[0]][0]:
                    cityLen[e[0]][0] = cityLen[u][0] + e[1]
                    cityLen[e[0]][1].clear()
                    cityLen[e[0]][1].extend(cityLen[u][1])
                    cityLen[e[0]][1].append(e[0])
                    stack.append(e[0])
            x += 1
        if start == end:
            total += 0
        else:           
            total += cityLen[end][0]
            print(cityLen[end])
            path = cityLen[end][1]
            for g in range(1, len(path)):
                for y in range(0, len(cities[path[g-1]])):
                    if cities[path[g-1]][y][0] == path[g]:
                        cities[path[g-1]][y] = (path[g], 0)
                for y in range(0, len(cities[path[g]])):
                    if cities[path[g]][y][0] == path[g-1]:
                        cities[path[g]][y] = (path[g-1], 0)
        for key in cityLen.keys():
            cityLen[key] = [sys.maxsize, []]
    cityLen = citysave.copy()
    cities = save.copy()
    #print(cities)
    print(total)