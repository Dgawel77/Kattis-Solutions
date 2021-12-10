def test(number):
    previous = set()
    for num in str(number):
        if num in previous:
            return False
        if num == "0":
            return False
        elif number % int(num) != 0:
            return False
        previous.add(num)
    return True

R = list(map(int, input().split()))
total = 0
for x in range(R[0], R[1]+1):
    if test(x):
        total += 1
print(total)
