def giveRem(side, rem, starting):
    global driven
    mmP = 1
    while rem > 0 and mmP < len(side):
        sideRem = side[mmP][1] % capacity
        if rem >= (sideRem):
            driven += 2*side[mmP][0] - (2*starting)
            side[mmP][1] -= sideRem
            starting = side[mmP][0]
            if side[mmP][1] == 0:
                side.remove(side[mmP])
            rem -= sideRem
            mmP += 1
        else:
            break
    return


def compute(side):
    global driven, capacity
    mmP = 0
    while len(side) > 0:
        driven += 2 * side[mmP][0] * (side[mmP][1] // capacity)
        remaining = 0
        if (side[mmP][1] % capacity) > 0:
            remaining = capacity - (side[mmP][1] % capacity)
        if remaining == 0:
            side.remove(side[mmP])
        else:
            driven += 2 * side[mmP][0]
            if len(side) > 1:
                giveRem(side, remaining, side[mmP][0])
            side.remove(side[mmP])
    return


given = list(map(int, input().split()))
capacity = given[1]
adresses = given[0]
#print(266*998*2 + 267*999*2 + 267*1000*2 + 267*1001*2 + 267*1002*2)
left = []
right = []
for _  in range(0, adresses):
    line = list(map(int, input().split()))
    addy = line[0]
    needed = line[1]
    if addy < 0:
        left.append([abs(addy), needed])
    else:
        right.append([addy, needed])
left.sort()
right.sort()

driven = 0
if len(left) > 0:
    compute(left)
if len(right) > 0:
    compute(right)
print(driven)
        