# line = input().split("-")
# str = ""
# for l in line:
#     str += l[0]
# print(str)

print(max(map(lambda x: int(x[::-1]),input().split())))