from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

R = int(input())
for _ in range(0, R):
    num = int(input())
    total = 1
    for x in factors(num):
        if len(factors(x)) > 2:
            total += 1
    print(total)

