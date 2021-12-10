def click(p, sequence):
    changing = list(sequence)
    g = {"A":a, "B":b, "C":c,"D":d, "E":e, "F":f}
    g[changing[p]](p, changing)
    return "".join(changing)

def a(p,changing):
    if p not in [0, 7]:
        changing[p-1] = rotate(changing[p-1])
        changing[p+1] = rotate(changing[p+1])
    elif p == 0:
        changing[p+1] = rotate(changing[p+1])
    else:
        changing[p-1] = rotate(changing[p-1])
            
def b(p,changing):
    if p not in [0, 7]:
        changing[p+1] = changing[p-1]
            
def c(p,changing):
    changing[7-p] = rotate(changing[7-p])
        
def d(p,changing):
    if p not in [0, 7]:
        if p >= 4:
            for x in range(p+1, 8):
                changing[x] = rotate(changing[x])
        else:
            for x in range(0, p):
                changing[x] = rotate(changing[x])
                    
def e(p,changing):
    if p not in [0, 7]:
        if p >= 4:
            y = 7 - p
        else:
            y = p
        changing[p+y] = rotate(changing[p+y])
        changing[p-y] = rotate(changing[p-y])
            
def f(p,changing):
    p += 1
    if p % 2 == 1:
        changing[((p+9)//2)-1] = rotate(changing[((p+9)//2)-1])
    else:
        changing[(p//2)-1] = rotate(changing[(p//2)-1])


def rotate(l):
    letter = ["A", "B", "C", "D", "E", "F"]
    return letter[(letter.index(l) + 1) % 6]


given = input()
target = input()
all = [(given, 0)]
inAll = set()
inAll.add(given)

j = 0
breakOut = False

if given == target:
    print(0)
    breakOut=True

while not breakOut:
    letters = all[j]
    j+=1
    for i in range(0, 8):
        got = click(i, letters[0])
        if got not in inAll:
            inAll.add(got)
            all.append((got, letters[1]+1))
        if got == target:
            print(letters[1]+1)
            breakOut = True
            break