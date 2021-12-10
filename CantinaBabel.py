R = int(input())
graph = {}
uds = {}
for _ in range(0, R):
    line = input().split()
    graph[line[0]] = set()
    for lang in line[1:]:
        if lang not in uds:
            uds[lang] = set()
        uds[lang].add(line[0])
    graph[line[0]] = graph[line[0]].union(uds[line[1]])
    graph[line[0]].remove(line[0])
print(graph)
#.remove(line[0])