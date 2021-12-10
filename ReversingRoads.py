def DFS(n):
    global mark, S, graph
    mark.add(n)
    for c in graph[n]:
        if c not in mark:
            DFS(c)
    S.append(n)
    
def DFSutil(n):
    global mark, revGraph
    mark.add(n)
    print(str(n) + " ", end="")
    for c in revGraph[n]:
        if c not in mark:
            DFSutil(c)


while True:
    try:
        m, n = map(int, input().split())
    except:
        break
    graph = {}
    revGraph = {}
    order = []
    for _ in range(0, n):
        a, b = map(int, input().split())
        order.append((a, b))
        if a not in graph:
            graph[a] = set()
            revGraph[a] = set()
        if b not in graph:
            graph[b] = set()
            revGraph[b] = set()
        graph[a].add(b)
        revGraph[b].add(a)
    S = []
    mark = set()
    DFS(order[0][0])
    print(S)
    mark = set()
    x = len(S)-1
    while x >= 0:
        DFSutil(S[x])
        print()
        x-=1
    print()
            
