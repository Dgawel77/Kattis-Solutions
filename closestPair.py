while (True):
    n = int(input())
    if (n == 0):
        break
    p = []
    for _ in range(0, n):
        pair = list(map(float, input().split()))
        p.append((pair[0], pair[1]))
    p.sort()
    print(p)
    
    