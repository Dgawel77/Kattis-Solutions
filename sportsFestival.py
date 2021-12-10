def compute(given):
    sum = 0
    for x in range(1, len(given)+1):
        sum += max(given[:x]) - min(given[:x])
    return sum

R = int(input())
nums = list(map(int, input().split()))
nums.sort()
output = []
for x in range(0, R):
    print(len(nums)//2)
    output.append(nums[len(nums)//2])
    nums.remove(nums[len(nums)//2])
print(output)
print(compute(output))