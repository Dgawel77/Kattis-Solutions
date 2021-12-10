def solve(t):
    global used
    
    
R = int(input())
used = set()
for x in range(0, R):
    L = int(input())
    s = input()
    fail = False
    if s.count('M') != L/3:
        print("NO")
        fail = True
    if not fail:
        Ts = 0
        for pos, char in enumerate(s):
            if char == "T":
                Ts += 1
            else:
                if Ts <= 0:
                    print("NO")
                    fail = True
                    break
                Ts -= 1
    if not fail:
        Ts = 0
        for pos, char in enumerate(s[::-1]):
            if char == "T":
                Ts += 1
            else:
                if Ts <= 0:
                    print("NO")
                    fail = True
                    break
                Ts -= 1
    if not fail:
        print("YES")
    