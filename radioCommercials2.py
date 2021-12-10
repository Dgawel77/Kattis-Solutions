n, p = map(int, input().split())
sAmount = list(map(int, input().split()))
solTable = [0 if sAmount[0]-p < 0 else sAmount[0]-p]
max = solTable[0]
for x in range(1, n):
    sum = solTable[x-1] + sAmount[x] - p
    if sum < 0:
        solTable.append(0)
    else:
        solTable.append(sum)
        if sum > max:
            max = sum
print(max)