def solve(chosen, remaining, changes, i):
    global R, best, routines, intersections
    if changes >= best:
        return
    if i==R:
        if changes < best:
            best = changes
        return
    for j in sorted(remaining):
        chosen[i] = j
        remaining.remove(j)
        if i > 0:
            solve(chosen, remaining, changes + intersections[j][chosen[i-1]], i+1)
        else:
            solve(chosen, remaining, changes, i+1)
        remaining.add(j)
    
R = int(input())

best = 0
routines = []
intersections = [[0 for i in range(R)] for j in range(R)]
for i in range(R):
    r = set(input())
    best += len(r)
    routines.append(r)
    for j in range(i):
        intersect = len(routines[j].intersection(r))
        intersections[j][i] = intersect
        intersections[i][j] = intersect
print(intersections)    

sequence = [0 for j in range(R)]
solve(sequence, set(range(R)), 0, 0)
print(best)
