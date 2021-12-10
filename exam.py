R = int(input())
Me = input()
Friend = input()
same = 0
diffrent = 0
for x in range(0, len(Me)):
    if Me[x] == Friend[x]:
        same += 1
    else:
        diffrent += 1
if same >= R:
    print(R + diffrent)
else:
    print(same + diffrent - (R -same))