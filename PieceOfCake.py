# import sys
# sys.setrecursionlimit(2600)
# total = 0
# times = 0
# def work(vect, pos):
#     global n, k, total, times, d
#     if pos < n and len(vect) < k:
#         vect.append(pos)
#         work(vect, pos + 1)
#         vect.remove(pos)
#         work(vect, pos + 1)
#     elif len(vect) == k:
#         area = 0
#         for x in range(1, k-1):
#             if (vect[0], vect[x], vect[x+1]) not in d:
#                 area += calcArea(vect[0], vect[x], vect[x+1])
#             else:
#                 area += d[vect[0], vect[x], vect[x+1]]
#         total += area
#         times += 1

# def calcArea(p1, p2, p3):
#     global points
#     x1, y1 = points[p1][0], points[p1][1]
#     x2, y2 = points[p2][0], points[p2][1]
#     x3, y3 = points[p3][0], points[p3][1]
#     a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
#     b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
#     c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
#     s = (a + b + c) / 2
#     area = (s * (s-a) * (s-b) * (s-c))**0.5
#     d[(p1, p2, p3)] = area
#     return area

# n, k = map(int, input().split())
# points = []
# d = {}
# for _ in range(n):
#     points.append(tuple(map(float, input().split())))

# work([], 0)
# print(total/times)
import random
from decimal import Decimal

def cross(a, b):
    return (a[0]*b[1]) - (a[1]*b[0])

n, k = map(int, input().split())
P = [(0, 0) for _ in range(2555)]
C = [[0 for _ in range(2555)] for _ in range(2555)]
for x in range(n):
    P[x] = (tuple(map(Decimal, input().split())))
    #P[x] = (Decimal(random.uniform(-10, 10)), Decimal(random.uniform(-10, 10)))

C[0][0] = Decimal(1)
for r in range(1, n+1):
    C[r][0] = Decimal(1)
    for c in range(1, r+1):
        C[r][c] = C[r-1][c] + C[r-1][c-1]

res = Decimal(0)
for i in range(0, n):
    for j in range(k-1, n):
        x = (i + j) % n
        res += (cross(P[i], P[x]) * C[j-1][k-2] / C[n][k])

print(res / Decimal(2))