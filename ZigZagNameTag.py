#compute is never used only have it for debugging
def compute(tag):
    sum = 0
    for x in range(0, len(tag)-1):
        sum += abs((ord(tag[x])-96) - (ord(tag[x+1])-96))
    return sum

n = int(input())
if n <= 25:
    tag = "a" + chr(97+n)
    print(tag)
else:
    offset = n % 25
    if offset == 0:
        offset = 25
        rep = (n // 25) - 1
    else:
        rep = n // 25
    tag = "a" + chr(offset//2 + 110) + ("a" if offset % 2 == 1 else "b")
    for i in range(1, rep):
        if tag[-1] == "a":
            tag = tag[:-1] + "az"
        elif tag[-1] == "b":
            tag = tag[:-1] + "ay"
        elif tag[-1] == "y":
            tag = tag[:-1] + "zb"
        elif tag[-1] == "z":
            tag = tag[:-1] + "za"
    print(tag)

#A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
