line  = input()
chars = line.split()
letters = chars[0]
password = chars[1]
point = 0
passed = False
for letter in enumerate(password):
    if letter[1] == letters[point]:
        point += 1
    elif letter[1] in letters[point:]:
        print("FAIL")
        passed = True
        break
    if point == len(letters):
        print("PASS")
        passed = True
        break
if not passed:
    print("FAIL")

