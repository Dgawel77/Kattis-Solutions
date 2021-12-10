def makeWalls():
    global walls
    WallCords = []
    while len(WallCords) != WallsNum:
        WallLine = list(map(int, input().split()))
        for i in range(0, len(WallLine), 4):
            WallCords.append(
                ((WallLine[i], WallLine[i+1]), (WallLine[i+2], WallLine[i+3])))
            #WallCords.append((WallLine[i+2], WallLine[i+3]))
    for Cord in WallCords:
        start = Cord[0]
        end = Cord[1]
        if start[0] - end[0] == 0:
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                walls[(start[0], y)] = True
        elif start[1] - end[1] == 0:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                walls[(x, start[1])] = True
        else:
            xslope = 1 if (start[0]- end[0]) < 0 else -1
            yslope = 1 if (start[1] - end[1]) < 0 else -1
            x = start[0]
            y = start[1]
            for _ in range(0, max(start[0], end[0])):
                walls[(x, y)] = True
                x += xslope
                y += yslope

def makeWetTiles():
    global total, walls, leaks, done, next
    next = {}
    for leak in leaks:
        for value in [-1, 1]:
            check((leak[0]+value, leak[1]))
            check((leak[0], leak[1]+value))
    for cord in leaks:
        done[cord] = True
    leaks.clear()
    for cord in next:
        leaks.append(cord)

def check(cord):
    global total
    try: 
        walls[cord]
    except:
        try:
            done[cord]
        except:
            if not outside(cord):
                try:
                    try:
                        next[cord]
                    except:
                        #print(cord)
                        next[cord] = True
                        total += 1
                except:
                    return

def outside(cord):
    global Width, Length
    if cord[0] > Width or cord[0] < 1:
        return True
    if cord[1] > Length or cord[1] < 1:
        return True

def printChart():
    global Width, Length, orgleaks
    actual = 0
    for y in reversed(range(0, Length+2)):
        for x in range(0, Width+2):
            try:
                if done[x, y]:
                    if (x, y) in orgleaks:
                        print("L", end="")
                    else:
                        print("x", end="")
                    actual += 1
            except:
                try: 
                    if walls[x, y]:
                        print("W", end="")
                except:
                    print(".", end="")
        print()
    return actual

while True:
    parameters = list(map(int, input().split()))
    if parameters == [-1]:
        break
    #Define Parameters
    Width = parameters[0]
    Length = parameters[1]
    Time = parameters[2]
    LeaksNum = parameters[3]
    WallsNum = parameters[4]
    LeaksLine = list(map(int, input().split()))
    total = 0
    #Get Leak Cords
    leaks = []
    orgleaks = []
    done = {}
    for i in range(0, LeaksNum*2, 2):
        leaks.append((LeaksLine[i], LeaksLine[i+1]))
        orgleaks.append((LeaksLine[i], LeaksLine[i+1]))
    #Get Wall Cords and make Walls
    walls = {}
    if WallsNum > 0:
        #Make Wet Squares
        makeWalls()
    #print(walls)
    #print(len(walls))
    next = {}
    for _ in range(0, Time):
        makeWetTiles()
    #print(printChart())
    #print(total)
    #print(len(leaks))
    print(len(done))