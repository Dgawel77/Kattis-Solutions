def forward(x, y):
    global facing, text
    while text[x][y] != "x":
        if text[x][y] in [".", "*"]:
            x, y = push(x, y)
        elif text[x][y] == "\\":
            if facing == 2:
                facing = 1
            elif facing == 0:
                facing = 3
            elif facing == 1:
                facing = 2
            elif facing == 3:
                facing = 0
            x, y = push(x, y)
        elif text[x][y] == "/":
            if facing == 2:
                facing = 3
            elif facing == 0:
                facing = 1
            elif facing == 1:
                facing = 0
            elif facing == 3:
                facing = 2
            x, y = push(x, y)
    changer = list(text[x])
    changer[y] = '&'
    text[x] = "".join(changer)
    return

def push(x, y):
    global facing
    if facing == 0:
        return(x, y-1)
    elif facing == 1:
        return(x+1, y)
    elif facing == 2:
        return(x, y+1)
    elif facing == 3:
        return(x-1, y)

Housenum = 0
while(True):
    size = input().split()
    Housenum+=1
    if size == ["0","0"]:
        break
    text = []
    enterance = 0
    for x in range(0, int(size[1])):
        given = input()
        if "*" in given:
            enterance = (x, given.find("*"))
        text.append(given)
    facing = 0
    if enterance[0] == 0:
        facing = 1
    elif enterance[1] == 0:
        facing = 2
    elif enterance[0] == int(size[1])-1:
        facing = 3
    forward(enterance[0], enterance[1])
    print("HOUSE " + str(Housenum))
    for line in text:
        print(line)