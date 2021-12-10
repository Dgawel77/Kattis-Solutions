R = int(input())
for _ in range(0, R):
    m = int(input())
    h = list(map(int, input().split()))
    evens = []
    odds = []
    for num in h:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    output = odds + evens
    for x in output:
        print(x, end=" ")
    print()
        