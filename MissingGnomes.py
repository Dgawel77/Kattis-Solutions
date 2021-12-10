n, m = map(int, input().split())
order = [0]
given = set()
count = 0
for x in range(0, m):
    num = int(input())
    order.append(num)
    given.add(num)

Maxi = 0
for pos in range(1, len(order)):
    for num in range(max(order[pos-1], Maxi)+1, order[pos]):
        if num not in given:
            print(num)
    print(order[pos])
    Maxi = max(order[pos], Maxi)

for num in range(Maxi+1, n+1):
    print(num)