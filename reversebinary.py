# R = int(input())
# sum = 0
# for pos, x in enumerate(str(bin(R))[2:]):
#     if x == "1":
#         sum += 2 ** (pos)
# print(sum)

print(int((str(bin(int(input())))[2:][::-1]), base=2))
