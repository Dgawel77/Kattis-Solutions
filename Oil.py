import math
maximumValue = 0
#calculates the Polar Cordinate Degree as varying scale of 0 - 180
#with the refrence being the x axis
#so a center of 0, 0 and point 30, 30 will give 45 degrees
#and a center of 0, 0 and point -30, -30 will also give 45 degrees
#to change it into a scale of 0 - 360 change the 180 to a 360
#so a center of 0, 0 and point 30, 30 will give 45 degrees
#and a center of 0, 0 and point -30, -30 will give 225 degrees

def calcPolarCordDegree(x1, y1, x2, y2):
    rad = math.atan2(y2 - y1, x2 - x1)
    if rad < 0:
        return math.pi + rad #change this to go to 0 - 360
    return rad

def solve(point):
    global maximumValue, points
    px, py, pvalue = point
    tempPoints = []
    for x, y, value in points:
        if y != py:
            if (y < py):
                value = -value
            tempPoints.append((calcPolarCordDegree(px, py, x, y), value))
    currentValue = abs(pvalue)
    maximumValue = max(maximumValue, currentValue)
    tempPoints.sort(reverse=True)
    for x, value in tempPoints:
        currentValue += value
        maximumValue = max(maximumValue, currentValue)

n = int(input())
points = []
for p in range(0, n):
    x1, x2, y = map(int, input().split())
    if (x1 > x2):
        x1, x2 = x2, x1
    value = x2 - x1
    points.append((x1, y, value))
    points.append((x2, y, -value))

for point in points:
    solve(point)

print(maximumValue)