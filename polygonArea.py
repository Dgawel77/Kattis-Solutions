while(True):
    n = int(input())
    if n == 0: 
        break
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    
    sum1 = 0
    sum2 = 0
    for p in range(0, n-1):
        sum1 += points[p][0] * points[p+1][1]
        sum2 += points[p][1] * points[p+1][0]
    sum1 += points[n-1][0] * points[0][1]
    sum2 += points[0][0] * points[n-1][1]
    area = (sum1 - sum2) / 2
    
    if area < 0:
        print("CW {0:.1F}".format(abs(area)))
    else:
        print("CCW {0:.1F}".format(abs(area)))