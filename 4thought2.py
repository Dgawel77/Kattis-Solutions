def solve(num):
    for x in ['*', '-', '+', '//']:
        for y in ['*', '-', '+', '//']:
            for z in ['*', '-', '+', '//']:
                total = int(eval(f'{num}{x}{num}{y}{num}{z}{num}'))
                if x == '//':
                    x = '/'
                if y == '//':
                    y = '/'
                if z == '//':
                    z = '/'
                results[total] = f'{num} {x} {num} {y} {num} {z} {num} = {int(total)}'
                if x == '/':
                    x = '//'
                if y == '/':
                    y = '//'
                if z == '/':
                    z = '//'


results = {}
solve("4")
R = int(input())
for _ in range(0, R):
    num = int(input())
    if num in results:
        print(results[num])
    else:
        print("no solution")