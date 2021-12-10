strings = []


def stringSub(LPos, prevLen, prevLetter):
    global strings
    lenNow = prevLen
    lenWith = prevLen
    lenWithOut = prevLen
    if LPos >= len(strings[0][0]):
        return prevLen
    L = strings[0][0][LPos]
    if all(map(lambda x: True if L in x[0][x[1]:] else False, strings)):
        lenWithOut = lenNow + stringSub(LPos+1, lenNow, L)
        for stringpak in enumerate(strings):
            pos = stringpak[0]
            string = stringpak[1][0]
            strings[pos] = (string, string.index(L)+1)
        lenWith = stringSub(LPos+1, lenNow + 1, L)
        for stringpak in enumerate(strings):
            pos = stringpak[0]
            string = stringpak[1][0]
            if prevLetter != "0":
                strings[pos] = (string, string.index(prevLetter)+1)
            else:
                strings[pos] = (string, 0)
    else:
        lenWithOut = lenNow + stringSub(LPos+1, lenNow, L)
    #print(lenWithOut if lenWithOut > lenWith else lenWith)
    return lenWithOut if lenWithOut > lenWith else lenWith


n, k = map(int, input().split())
print("AHFBGDCE"[1:])
for _ in range(0, n):
    strings.append((input(), 0))
biggestO = 0
print()
print(stringSub(0, 0, "0"))
# for L in strings[0][0]:
#     print(L)
#     print(strings)
#     if all(map(lambda x : True if L in x[0][x[1]:] else False, strings)):
#         length += 1
#         for stringpak in enumerate(strings):
#             pos = stringpak[0]
#             string = stringpak[1][0]
#             #print(string)
#             #print(string.index(L))
#             strings[pos] = (string, string.index(L)+1)

# HGBDFCAE
# ADBGHFCE
# HCFGBDAE

# HFCAE
# HFCE
# HFGBDAE

# ABCE
# ABGCEHD
# ABCE
# ABCE
# ABCEDG
# ABHCE

# AHFBGDCE 1
# FABGCEHD 2
# AHDGFBCE 1
# DABHGCFE 2
# ABCHFEDG 1
# DGABHFCE 4

# HGBDFCAE
# HFCE
# HCFGBDAE

# FCAE
# FCE
# FGBDAE

# E
# E
# E

# 6 8
# AHFBGDCE
# AHD
# AHDGFBCE
# ABHGCFE
# ABCHFEDG
# ABHFCE

# ABCE
# ABCEHD
# ABCE
# ABCFE
# ABCHFEDG
# ABCE
