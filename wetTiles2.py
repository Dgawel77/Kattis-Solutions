def makeWalls():
    WallCords = []
    while len(WallCords) != WallsNum:
        WallLine = list(map(int, input().split()))
        for i in range(0, len(WallLine), 4):
            WallCords.append(((WallLine[i], WallLine[i+1]), (WallLine[i+2], WallLine[i+3])))
    for Cord in WallCords:
        start = Cord[0]
        end = Cord[1]
        if start[0] - end[0] == 0:
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                table[y-1][start[0]-1] = "w"
        elif start[1] - end[1] == 0:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                table[start[1]-1][x-1] = "w"
        else:
            xslope = 1 if (start[0]- end[0]) < 0 else -1
            yslope = 1 if (start[1] - end[1]) < 0 else -1
            x = start[0]
            y = start[1]
            for _ in range(0, max(start[0], end[0])):
                table[y-1][x-1] = "w"
                x += xslope
                y += yslope

def makeTiles():
    global leaks, next
    for leak in leaks:
        for value in [-1, 1]:
            check(leak[0]+value, leak[1])
            check(leak[0], leak[1]+value)
    #print(next)
    leaks = next
    next = []
    return

def check(r, c):
    global total, next
    if not outside((c, r)):
        if table[c-1][r-1] == '.':
            table[c-1][r-1] = "x"
            next.append((r, c))
            total+=1

def outside(cord):
    global Width, Length
    if cord[0] > Width or cord[0] < 1:
        return True
    if cord[1] > Length or cord[1] < 1:
        return True

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
    #make array
    table = []
    for y in range(0, Length):
        table.append([])
        for x in range(0, Width):
            table[y].append(".")
    #Get Leak Cords
    LeaksLine = list(map(int, input().split()))
    leaks = []
    for i in range(0, LeaksNum*2, 2):
        table[LeaksLine[i+1]-1][LeaksLine[i]-1] = "x"
        leaks.append((LeaksLine[i], LeaksLine[i+1]))
    #Get Wall Cords and make Walls
    if WallsNum > 0:
        makeWalls()
    #make Tiles
    total = len(leaks)
    next = []
    for _ in range(0, Time-1):
        makeTiles()  
    #print
    for row in reversed(table):
        for char in row:
            print(char, end="")
        print()
    print(total)