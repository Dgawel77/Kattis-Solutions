import math
def primeFactors(n):
    global nums
    while n % 2 == 0:
        nums.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1,2):
        while n % i== 0:
            nums.append(i)
            n = n / i
    
    if n > 2:
        nums.append(int(n))

while True:
    try:
        number = int(input())
        if number < 0:
            print("-1", end=" ")
            number = number * -1
        nums = []
        primeFactors(number)
        numsSet = set(nums)
        for num in numsSet:
            exp = nums.count(num)
            if exp > 1:
                print('{0}^{1}'.format(num, exp), end=" ")
            else:
                print(num, end=" ")
        print()
    except EOFError:
        break
    