def DFS(program):
    global mark, post, graph, stack, clock
    clock += 1
    for w in graph[program]:
        if w not in mark:
            clock += 1
            mark.add(w)
            stack.append(program)
            stack.append(w)
            return
    clock += 1
    post.append((program ,clock))
    return 

programs = int(input())
graph, post, stack = {}, [], []
for i in range(programs):
    line = input().split()
    dpProgram = line[0][:-1]
    if dpProgram not in graph:
        graph[dpProgram] = set()
    for piece in line[1:]:
        if piece not in graph:
            graph[piece] = set()
        graph[piece].add(dpProgram)

mark = set()
clock = 0
stack.append(input())
while len(stack) != 0:
    DFS(stack.pop())

post.sort(key = lambda x: x[1], reverse = True)
for i in post:
    print(i[0])
