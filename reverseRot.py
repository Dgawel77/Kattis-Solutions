letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def solve(param):
    answer = ""
    for letter in enumerate(reversed(param[1])):
        answer = answer + letters[(letters.find(letter[1])+int(param[0])) % len(letters)]
    return answer

while True:
    text = input().split()
    if text == ['0']:
        break
    print(solve(text))