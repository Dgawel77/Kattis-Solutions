line = list(map(int, input().split()))
walls = set(map(int, input().split()))
R = line[0]
N = line[1]
A = line[2]
B = line[3]
graph = {}
prev = 0
rows = []
for add in list(range(0, R)) + list(range(R-2, -1, -1)):
    rows.append(list(range(prev+1, prev+R+add+1)))
    prev += add+R
for x in range(1, (R**3 - (R-1)**3)+1):
    graph[x] = []
for row in enumerate(rows):
    for x in range(0, len(row[1])):
        if x-1 >= 0:
            graph[row[1][x]].append(row[1][x-1])
        if x+1 < len(row[1]):
            graph[row[1][x]].append(row[1][x+1])
        if row[0]+1 < R:
            graph[row[1][x]].append(rows[row[0]+1][x])
            graph[row[1][x]].append(rows[row[0]+1][x+1])
            graph[rows[row[0]+1][x]].append(row[1][x])
            graph[rows[row[0]+1][x+1]].append(row[1][x])
        else:
            if row[0] <= (R*2)-3:
                if x < len(rows[row[0]+1]):
                    graph[row[1][x]].append(rows[row[0]+1][x])
                    graph[rows[row[0]+1][x]].append(row[1][x])
                if x-1 >= 0:
                    graph[row[1][x]].append(rows[row[0]+1][x-1])
                    graph[rows[row[0]+1][x-1]].append(row[1][x])

# for key in graph.keys():
#    print(key, graph[key])
stack = [(A, 0)]
mark = set()
mark.add(A)
move = True
out = "No"
while len(stack) > 0 and move:
    s = stack.pop(0)
    if s[0] == B:
        move = False
        out = s[1]
    for i in graph[s[0]]:
        if (i not in mark) and (i not in walls):
            stack.append((i, s[1]+1))
            mark.add(i)
        if i == B:
            move = False
            if s[1] < N:
                out = s[1]+1
    if s[1] >= N:
        break
print(out)