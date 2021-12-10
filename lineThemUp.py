times = input()
names = []
sortNames = []
revSortNames = []
for _ in range(0, int(times)):
    name = input()
    names.append(name)
    sortNames.append(name)
    revSortNames.append(name)
sortNames.sort()
revSortNames.sort(reverse=True)
if sortNames == names:
    print("INCREASING")
elif revSortNames ==  names:
    print("DECREASING")
else:
    print("NEITHER")
    