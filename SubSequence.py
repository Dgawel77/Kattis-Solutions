#global A, B
def LCS(Ai, Bj):
    global A, B
    if Ai >= len(A) or Bj >= len(B):
        return 0
    if A[Ai] == B[Bj]:
        Ai += 1
        Bj += 1
        return 1 + LCS(Ai, Bj)
    else:
        Ai += 1
        NextInA = LCS(Ai, Bj)
        Ai -= 1
        Bj += 1
        NextInB = LCS(Ai, Bj)
        return max(NextInA, NextInB)


StringA = input()
StringB = input()

A = []
B = []

for x in StringA:
    A.append(x)
for x in StringB:
    B.append(x)

print(LCS(0, 0))
