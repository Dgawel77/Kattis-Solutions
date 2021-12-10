given = input().split()
if int(given[0]) + int(given[1]) == 0:
    print("Not a moose")
elif given[0] == given[1]:
    print("Even " + str(int(given[0]) + int(given[1])))
elif given[0] > given[1]:
    print("Odd " + str(max(int(given[0]), int(given[1]))*2))
elif given[0] < given[1]:
    print("Odd " + str(max(int(given[0]), int(given[1]))*2))
