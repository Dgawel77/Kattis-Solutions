def solve(act, groupsLeft, quickChanges):
    global bestSoFar
    if quickChanges >= bestSoFar:
        return
    if len(groupsLeft) == 0 and quickChanges < bestSoFar:
        bestSoFar = quickChanges
        return
    for g in sorted(groupsLeft):
        act.append(g)
        groupsLeft.remove(g)
        if len(act) == 1:
            solve(act, groupsLeft, quickChanges)
        else:
            solve(act, groupsLeft, quickChanges + table[act[-2]][act[-1]])
        groupsLeft.append(g)
        act.remove(g)


x = input()
groups = []
bestSoFar = 2

table = [[0 for _ in range(int(x))] for _ in range(int(x))]
for i in range(int(x)):
    recital = set(input())
    bestSoFar += len(recital)
    groups.append(recital)
    for j in range(i):
        intersect = len(groups[j].intersection(recital))
        table[i][j] = intersect
        table[j][i] = intersect

solve([], list(range(0, int(x))), 0)
print(bestSoFar)