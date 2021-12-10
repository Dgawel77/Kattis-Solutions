for _ in range(int(input())):
    p = []
    n = int(input())
    for _ in range(0, n):
        p.append(list(map(int, input().split())))
    
    t = [[0 if c != n else r for c in range(0, n+1)] for r in range(0, 8)]
    for c in reversed(range(0, n)):
        for r in range(0, 8):
            outcomes = []
            for x in [1, 2, 4]:
                outcomes.append(t[r ^ x][c+1])
            favor = []
            for outcome in outcomes:
                favor.append(p[c][outcome])
            t[r][c] = outcomes[favor.index(min(favor))]
    # for row in t:
    #     print(row)
    prnt = ["NNN", "NNY", "NYN", "NYY", "YNN", "YNY", "YYN", "YYY"]
    print(prnt[t[0][0]])
    