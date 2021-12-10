def solve(time1, time2, angle):
    hour1 = int(time1[:2])
    minute1 = int(time1[3:])
    start = hour1*60 + minute1

    hour2 = int(time2[:2])
    minute2 = int(time2[3:])
    end = hour2*60 + minute2

    d0 = []
    time = 0
    if angle == 90:
        time += 180
        while time/11 <= end:
            d0.append(time)
            time += 360
    elif angle == 180:
        time += 360
        while time/11 <= end:
            d0.append(time)
            time += 720
    else:
        while time/11 <= end:
            d0.append(time)
            time += 720
    
    for num in d0:
    total = 0
        if start <= num/11 <= end:
            total += 1
    print(total)
     
R = input()
for _ in range(0, int(R)):
    Line = input().split()
    time1 = Line[0]
    time2 = Line[1]
    angle = int(Line[2])
    solve(time1, time2, angle)