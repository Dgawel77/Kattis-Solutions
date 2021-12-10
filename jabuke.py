xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())
area = abs(xA*(yB-yC) + xB*(yC-yA) + xC*(yA-yB)) / 2
print("{0:.1f}".format(area))

count = 0
for _ in range(int(input())):
    xP, yP = map(int, input().split())
    A1 = abs(xA*(yB-yP) + xB*(yP-yA) + xP*(yA-yB)) / 2
    A2 = abs(xA*(yP-yC) + xP*(yC-yA) + xC*(yA-yP)) / 2
    A3 = abs(xP*(yB-yC) + xB*(yC-yP) + xC*(yP-yB)) / 2
    if A1 + A2 + A3 == area:
        count += 1
print(count)