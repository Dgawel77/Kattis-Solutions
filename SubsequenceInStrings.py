s = input()
t = input()
table = [[-1 for _ in range(len(s)+1)] for _ in range(26)]
placed = set()
for pos, char in enumerate(s[::-1]):
    PosInString = len(s)-pos
    if PosInString - 1 >= 0:
        for num in placed:
            table[num][PosInString-1] = table[num][PosInString]
        table[(ord(char)-97)][PosInString-1] = PosInString
        placed.add(ord(char)-97)

ans = 0
before = 0
def calcOccurences(start, tpos, spos):
    global t, before, ans
    if tpos >= len(t):
        ans += (start - before) * (len(s) - spos + 1)
        before = start
        #print(start, tpos, spos)
    else:
        if table[ord(t[tpos])-97][spos] > -1:
            calcOccurences(start, tpos+1, table[ord(t[tpos])-97][spos])

pos = 0
while table[ord(t[0])-97][pos] != -1:
    calcOccurences(table[ord(t[0])-97][pos], 1, table[ord(t[0])-97][pos])
    pos = table[ord(t[0])-97][pos]

print(ans)

#for c, t in enumerate(table):
#    print(chr(c+97), t)
    
    
# penpineappleapplepen
# ppap
# left * right
# 1 * 12
# 3 * 7
# 5 * 7