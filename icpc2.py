n = int(input())
rang = set(range(1, n+1))
nums = input()
for i in range(1, n+2):
    if not nums[:len(''.join(str(x) for x in range(1, i)))] == ''.join(str(x) for x in range(1, i)):
        print(i-1)
        break