from typing import Deque

output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def solve(list):
    if len(list) == 1:
        output[list[0]] += 1
        return
    a = list.popleft()
    b = list.popleft()
    ans = (a + b) % 10
    list.appendleft(ans)
    solve(list)
    list.popleft()
    ans = (a * b) % 10
    list.appendleft(ans)
    solve(list)
    list.popleft()
    list.appendleft(b)
    list.appendleft(a)

N = int(input())
nums = Deque(map(int, input().split()))
solve(nums)
for c in output:
    print(c)