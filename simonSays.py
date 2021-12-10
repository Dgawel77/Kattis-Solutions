R = int(input())
for _ in range(0, R):
    line = input()
    if line[:10] == "Simon says":
        print(line[10:])