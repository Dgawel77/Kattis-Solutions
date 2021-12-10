n, k = map(int, input().split())
fib = [0, 1, 1]
for _ in range(3, n+1):
    fib.append(fib[-1]+fib[-2])

while n > 2:
    tmp = fib[n-2]
    if k > tmp:
        n -= 1
        k -= tmp
    else:
        n -= 2

if n == 1:
    print('N')
else:
    print('A')