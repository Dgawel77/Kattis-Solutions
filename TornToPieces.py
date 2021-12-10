def DFS(station, path, count):
    global GoTo, bestPath, bestCount
    mark[station] = True
    count += 1
    path = path + " " + station
    if station == GoTo:
        return count
    for route in routes[station]:
        if not mark[route]:
            temp = DFS(route, path, count)
            if temp < count:
                count = temp
    return count

numPieces = int(input())
liststations, routes, mark =[], {}, {}
bestPath = ""
bestCount = 10000000
for i in range(numPieces):
    pieces = input().split()
    routes[pieces[0]] = set()
    mark[pieces[0]] = False
    liststations.append(pieces[0])
    for piece in pieces[1:]:
        if(piece not in routes):
            routes[piece] = set()
            mark[piece] = False
            liststations.append(piece)
        routes[pieces[0]].add(piece)
        routes[piece].add(pieces[0])
Start, GoTo = tuple(input().split())
print(DFS(Start, "", 0))
