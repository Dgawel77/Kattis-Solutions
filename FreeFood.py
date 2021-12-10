R = int(input())
total = set()
for _ in range(0, R):
    line = list(map(int, input().split()))
    total = total.union(range(line[0], line[1]+1))
print(len(total))
