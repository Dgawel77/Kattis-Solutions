def BFS(s, w):
    global dist, graph, shortestPath, shortElement
    initSSSP(s)
    queue = []
    queue.append(s)
    while len(queue) != 0:
        u = queue.pop()
        if u == w:
            if dist[u][0]+1 < shortest:
                shortestPath = dist
                shortElement = u
                return
        for v in graph[u]:
            if v == w:
                if dist[v][0]+1 < shortest:
                    dist[v] = (dist[u][0] + 1, u)
                    shortestPath = dist
                    shortElement = v
                    return
            if dist[v][0] > dist[u][0] + 1:
                dist[v] = (dist[u][0] + 1, u)
                queue.append(v)


def initSSSP(s):
    dist[s] = (0, "")
    for v in graph.keys():
        if v != s:
            dist[v] = (10000000, "")


R = input()
graph = {}
dist = {}
G = input().split()
for file in G:
    graph[file] = []
for _ in range(0, len(G)):
    line = input().split()
    for _ in range(0, int(line[1])):
        impLine = (input() + ",").split()
        for file in impLine[1:]:
            graph[line[0]].append(file[:-1])

shortestPath = {}
shortElement = ""
shortest = 1000000000000

for key in graph.keys():
    for edge in sorted(graph[key]):
        dist = {}
        graph[key].remove(edge)
        BFS(edge, key)
        graph[key].append(edge)

if shortElement == "":
    print("SHIP IT")
else:
    answer = ""
    nextNode = shortestPath[shortElement]
    while shortestPath[shortElement] != (0, ''):
        answer = shortElement + " " + answer
        shortElement = shortestPath[shortElement][1]
    print(shortElement + " " + answer)
