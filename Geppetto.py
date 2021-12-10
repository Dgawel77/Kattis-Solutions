def solve(partialSol, i):
    global total, ingredients, forbidden, Length
    if i == Length:
        return
    cont = True
    for x in range(i, Length):
        cont = True
        for previous in partialSol[:i]:
            if (previous in forbidden[ingredients[x]] or previous == ingredients[x] or previous > ingredients[x]):
                cont = False
                break
        print(i, end = ' ')
        print(ingredients[x], end = ' ')
        print(previous in forbidden[ingredients[x]], end = ' ')
        print(previous == ingredients[x], end = ' ')
        print(cont)
        if cont:
            partialSol[i] = ingredients[x]
            total+=1
            print(partialSol)
            solve(partialSol, i+1)
            #print(partialSol)
            partialSol[i] = 0
    return
    
while True:
    try:
        n1, n2 = tuple(input().split())
    except:
        break
    Length = int(n1)
    total = 0
    ingredients, forbidden = [],{}
    
    for i in range(1, Length+1):
        ingredients.append(i)
        forbidden[i] = set()
    ingredients.sort()
    
    for i in range(int(n2)):
        m1, m2 = tuple(input().split())
        forbidden[int(m1)].add(int(m2))
        forbidden[int(m2)].add(int(m1))
        
    partialSol = []
    for i in range(Length):
        partialSol.append(0)
        
    solve(partialSol, 0)
    print(total+1)
