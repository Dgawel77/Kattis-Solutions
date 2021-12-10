def decifer(words):
    global dictShort
    correct = dictShort[words[0]][0]
    incorrect = dictShort[words[0]][1]
    for word in words[1:]:
        tmpCorrect = correct
        tmpCorrect = tmpCorrect * dictShort[word][0]
        incorrect = correct * dictShort[word][1] + incorrect * dictShort[word][1] + incorrect * dictShort[word][0]
        correct = tmpCorrect
    return (correct, incorrect)


def translate(words, current):
    global dict
    if len(words) == 0:
        return current
    return translate(words[1:], current + " " + str(dict[words[0]][0][0]))


Rwords = int(input())
sentence = input().split()
Dwords = int(input())
dict = {}
dictShort = {}
for _ in range(0,Dwords):
    line = input().split()
    if line[0] not in dict:
        dict[line[0]] = []
        dictShort[line[0]] = [0, 0]
    if line[2] == "correct":
        dictShort[line[0]][0] += 1
    else:
        dictShort[line[0]][1] += 1
    dict[line[0]].append((line[1], True if line[2] == "correct" else False))
numTup = decifer(sentence)
if numTup[0] == 1:
    print(translate(sentence, "")[1:])
    print("correct")
elif numTup[1] == 1:
    print(translate(sentence, "")[1:])
    print("incorrect")
else:
    print(str(numTup[0]) + " correct")
    print(str(numTup[1]) + " incorrect")