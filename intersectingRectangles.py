n = int(input())
tree = [0] * (2 * n)


class rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def build(arr):
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


def updateTreeNode(p, value):
    tree[p + n] = value
    p = p + n
    i = p
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


def query(l, r):
    res = 0
    l += n
    r += n

    while l < r:
        if (l & 1):
            res += tree[l]
            l += 1
        if (r & 1):
            r -= 1
            res += tree[r]
        l >>= 1
        r >>= 1
    return res


build([0] * 2 * n)
verticalLines = []

oldMinValue = 10**9
oldMaxValue = -10**9

for x in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rec = rectangle(x1, y1, x2, y2)
    verticalLines.append((x1, rec, False))
    verticalLines.append((x2, rec, True))
    oldMinValue = min(oldMinValue, y1)
    oldMaxValue = max(oldMaxValue, y2)

verticalLines.sort()
for xLine, rec, addOrRemove in verticalLines:
    # remove from tree
    if addOrRemove:

        pass
    # add to tree
    else:
        print(rec.y1, remap(rec.y1, -10**9, 10**9, 0, 2*(10**5)))
        pass


#print(query(1, 3))
#updateTreeNode(2, 1)
# function to get sum on interval [l, r)
#print(query(1, 3))
