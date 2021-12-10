N = int(input())
nums = list(map(int, input().split()))
minSoFar = [0] * N
maxSoFar = [0] * N
maxNow = 0
for p, n in enumerate(nums):
    maxNow = max(maxNow, n)
    maxSoFar[p] = maxNow
minNow = 2**32 - 1
for p, n in list(enumerate(nums))[::-1]:
    minNow = min(minNow, n)
    minSoFar[p] = minNow

count = 0
if nums[0] < minSoFar[1]:
    count += 1
for p in range(1, N-1):
    if maxSoFar[p] <= nums[p] < minSoFar[p+1]:
        count += 1
if maxSoFar[N-2] <= nums[N-1]:
    count += 1
print(count)