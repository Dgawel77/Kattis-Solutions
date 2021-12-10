woodCuttingTimes = []
total = 0
testCases = int(input())
for i in range(testCases):
    numberOfCustomers = int(input())
    for j in range(numberOfCustomers):
        listOfCuts = list(map(int, input().split()))
        for k in listOfCuts:
            total += k
        total -= listOfCuts[0]
        woodCuttingTimes.append(total)
        total = 0
    totalTime = 0
    currentTimeElapsed = 0
    woodCuttingTimes.sort()
    for k in woodCuttingTimes:
        totalTime += currentTimeElapsed + k
        currentTimeElapsed += k
    print(totalTime / len(woodCuttingTimes))
    woodCuttingTimes.clear()
