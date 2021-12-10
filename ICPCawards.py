R = int(input())
teams = set()
count = 0
for x in range(0, R):
    uni, team = input().split()
    if count <= 11:
        if uni not in teams:
            print(uni + " " + team)
            count += 1
            teams.add(uni)