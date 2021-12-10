n, m = map(int, input().split())
for _ in range(0, n):
    input()
CityToCity = []
for _ in range(0, m):
    line = input().split()
    CityToCity.append((int(line[2]), line[0] + " " + line[1]))
    #CityToCity.append((int(line[2]), line[1] + " " + line[0]))
assignment = set()
for _ in range(0, 4):
    line = input().split()
    assignment.add(line[0])
    assignment.add(line[1])
city = set()
CityToCity.sort()

total = 0
x = 0
while not assignment.issubset(city):
    u = CityToCity[x]
    bc = u[1].split()
    if bc[0] not in city and bc[1] not in city:
        print(bc)
        city.add(bc[0])
        city.add(bc[1])
        total += u[0]
    x += 1
print(city)
print(total)