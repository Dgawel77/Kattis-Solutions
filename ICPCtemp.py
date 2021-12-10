exampleTests = ["F", "T"]
def makeTest():
    for _ in range(0, k):
        lent = len(exampleTests)
        for x in range(0, lent):
            exampleTests.append(exampleTests[x])
        for x in range(0, len(exampleTests)//2):
            exampleTests[x] = exampleTests[x]+"T"
        for x in range(len(exampleTests)//2, len(exampleTests)):
            exampleTests[x] = exampleTests[x]+"F"
        print(exampleTests)

k, n = map(int, input().split())
makeTest()
tests = []
for _ in range(0, k):
    tests.append(input())
allBest = 1000000000
for example in exampleTests:
    for test in tests:
        best = 0
        score = 0
        for L in enumerate(test):
            if L[1] == example[L[0]]:
                score += 1
        if best < score:
            best = score
    if allBest > best:
        allBest = best
print(allBest)

                
# 5032
# 0523    
# FTF
# TFTF
# TFFF1
# TFTT
# TFFT1
# TFTF

# TFTFT
# TFTFT
# TFTFT