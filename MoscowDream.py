line = input().split()
easy = int(line[0])
medium = int(line[1])
hard = int(line[2])
n = int(line[3])

if (easy <= 0) or (medium <= 0) or (hard <= 0):
    print("NO")
else:
    if((easy + medium + hard) > n and (n >= 3)):
        print("YES")
    else:
        print("NO")