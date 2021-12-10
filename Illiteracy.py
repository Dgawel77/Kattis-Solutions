def click(p, sequence):
    changing = list(sequence)
    if changing[p] == "A":
        if p not in [0, 7]:
            changing[p-1] = rotate(changing[p-1])
            changing[p+1] = rotate(changing[p+1])
        elif p == 0:
            changing[p+1] = rotate(changing[p+1])
        else:
            changing[p-1] = rotate(changing[p-1])
    elif changing[p] == "B":
        if p not in [0, 7]:
            changing[p+1] = changing[p-1]
    elif changing[p] == "C":
        changing[7-p] = rotate(changing[7-p])
    elif changing[p] == "D":
        if p not in [0, 7]:
            if p >= 4:
                for x in range(p+1, 8):
                    changing[x] = rotate(changing[x])
            else:
                for x in range(0, p):
                    changing[x] = rotate(changing[x])
    elif changing[p] == "E":
        if p not in [0, 7]:
            if p >= 4:
                y = 7 - p
            else:
                y = p
            changing[p+y] = rotate(changing[p+y])
            changing[p-y] = rotate(changing[p-y])
    elif changing[p] == "F":
        p += 1
        if p % 2 == 1:
            changing[((p+9)//2)-1] = rotate(changing[((p+9)//2)-1])
        else:
            changing[(p//2)-1] = rotate(changing[(p//2)-1])
    return "".join(changing)


def rotate(l):
    letter = ["A", "B", "C", "D", "E", "F"]
    return letter[(letter.index(l) + 1) % 6]


given = input()
target = input()
all = [(given, 0)]
inAll = {}
inAll[given] = True
if given == target:
    print(0)
    all.pop()
prev = 0
while len(all) != 0:
    breakOut = False
    letters = all.pop(0)
    for i in range(0, 8):
        got = click(i, letters[0])
        if got not in inAll:
            inAll[got] = True
            all.append((got, letters[1]+1))
        if got == target:
            print(letters[1]+1)
            breakOut = True
            break
    #if prev != letters[1]:
    #    prev = letters[1]
    #    print(letters[1])
    #    print(len(inAll), len(all))
    if breakOut:
        break
print(len(inAll))