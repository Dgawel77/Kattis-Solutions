R = int(input())
order = []
for _ in range(0, R):
    order.append(input())
order = order[::-1]
mult = 1
total = 0
for x in order:
    if x == "O":
        total += mult
    mult *= 2
print(total)