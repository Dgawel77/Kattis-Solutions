did = [[False for i in range(10)] for j in range(100)] 
memo = [[0 for i in range(10)] for j in range(100)]
n = 2
k = 2
def tight(ind, last):
    if last < 0 or last > k:
        return 0
    result = 0
    if ind == n:
        return 1
    if did[ind][last]:
        return memo[ind][last]
    result += tight(ind+1, last)
    result += tight(ind+1, last-1)
    result += tight(ind+1, last+1)
    did[ind][last] = True
    memo[ind][last] = result
    return result

while True:
    try:
        did = [[False for i in range(10)] for j in range(100)] 
        total = 0
        k, n = map(int, input().split())
        if n == 1:
            print("100.0")
            continue
        for i in range(k+1):
            total += tight(1, i)
        #print(total)
        print(total/((k+1)** n) * 100)
    except:
        break

