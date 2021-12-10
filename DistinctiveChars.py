R = input().split()
players = []
similarity = [0 for _ in range(0, int(R[1]))]
for _ in range(0, int(R[0])):
    G = input()
    for char in enumerate(G):
        if char[1] == "1":
            similarity[char[0]] += 1
        if char[1] == "0":
            similarity[char[0]] -= 1

for sim in similarity:
    if sim < 0:
        print("1", end="")
    else:
        print("0", end="")

