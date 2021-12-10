n, m = map(int, input().split())
order = []
given = set()
for x in range(0, m):
    num = int(input())
    order.append(num)
    given.add(num)

mark = 0
i = 1
while i < n:
    if i not in given and i < order[mark]:
        print(i)
        i+=1
    else:
        print(order[mark])
        mark+=1
    #print(i, mark)
