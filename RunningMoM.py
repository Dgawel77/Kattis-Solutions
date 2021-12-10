def DFS(city, clock):
    global mark, preAndpost, routes
    mark[city] = True
    clock += 1
    preAndpost[city][0] = clock
    for w in routes[city]:
        if not mark[w]:
            #preAndpost[city][2] = city
            clock = DFS(w, clock)
    clock += 1
    preAndpost[city][1] = clock
    return clock

numFlights = int(input())
routes, preAndpost, cities, mark = {}, {}, [], {}
for i in range(numFlights):
    c1, c2 = tuple(input().split())
    if(c1 not in cities):
        cities.append(c1)
        preAndpost[c1] = [1 for i in range(2)]
        routes[c1] = set()
        mark[c1] = False
    if(c2 not in cities):
        cities.append(c2)
        preAndpost[c2] = [1 for i in range(2)]
        routes[c2] = set()
        mark[c2] = False
    routes[c1].add(c2)

clock = 0
for city in cities:
    if not mark[city]:
        clock = DFS(city, clock)

#finds back edge
backEdges = []
for city in cities:
    for w in routes[city]:
        if preAndpost[w][0] < preAndpost[city][0] and preAndpost[city][1] < preAndpost[w][1]:
            backEdges.append([[preAndpost[w][0], preAndpost[city][0]], [preAndpost[city][1], preAndpost[w][1]]])

try:
    while True:
        checkCity = input()
        if checkCity == '':
            break
        for edge in backEdges:
            if preAndpost[checkCity][1] < edge[0][0]:
                print(checkCity + " trapped")
            elif preAndpost[checkCity][1] < edge[1][0]:
                print(checkCity + " trapped")
            elif edge[0][0] <= preAndpost[checkCity][0] <= edge[0][1]:
                print(checkCity + " safe")
            elif edge[1][0] <= preAndpost[checkCity][1] <= edge[1][1]:
                print(checkCity + " safe")
            else:
                print(checkCity + " trapped")
except EOFError:
    pass

print(preAndpost)
print(backEdges)
