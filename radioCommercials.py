global SolTable, Commercials
def solve():
    SolTable[int(N)] = 0
    for i in reversed(range(int(N))):
        #SolTable[i] = 0
        for j in range(i, int(N)):
            CurrentValue = int(Commercials[j]) + SolTable[j+1] - int(cost)
            if CurrentValue > SolTable[i]:
                SolTable[i]=CurrentValue
    return SolTable[1]  
    
    
N, cost = tuple(input().split())
Commercials = input().split()
SolTable = []
for i in range(int(N)+1):
    SolTable.append(0)
print(solve())
