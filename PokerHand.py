R = input().split()
unique = {}
for card in R:
    if card[0] not in unique:
        unique[card[0]] = 1
    else:
        unique[card[0]] += 1
print(max(unique.values()))