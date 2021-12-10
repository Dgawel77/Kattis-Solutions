def solve():
    global N, numbers, values, closest
    for j in range(1, N+1):
        for i in numbers[j-1]:
            numbers[j].add(i)
            withj = i + values[j]
            numbers[j].add(withj)
    for i in numbers[N]:
        closer(i)
    return closest+1000

def closer(i):
    global closest
    if(abs(i-1000) <= abs(closest)):
                if(abs(i-1000) == abs(closest)):
                    closest = max(closest, i-1000)
                else:
                    closest = i-1000

N = int(input())

numbers = []
values = []
numbers.append(set())
values.append(0)
numbers[0].add(0)
for i in range(N):
    i1 = int(input())
    numbers.append(set())
    values.append(i1)

closest = 1000000
print(solve())
