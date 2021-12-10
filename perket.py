def solve(position, sour, bitter):
    global smallestDif
    if position >= len(ingredients):
        if smallestDif > abs(sour - bitter):
            smallestDif = abs(sour - bitter)
        return 
    for ingredient in ingredients:
        solve(position+1, sour*ingredient[0], bitter+ingredient[1])
        solve(position+1, sour, bitter)

numIngredients = int(input())
ingredients = []
for x in range(numIngredients):
    ing = input().split()
    ingredients.append((int(ing[0]), int(ing[1])))

smallestDif = 100000000000000000
print()
if len(ingredients) > 1:
    solve(0, 1, 0)
    print(smallestDif)
else:
    print(abs(ingredients[0][0] - ingredients[0][1]))
