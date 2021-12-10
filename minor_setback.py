import math

num = int(input())
pitches = []
keys = {"G major": {10:"G", 0:"A", 2:"B", 3:"C", 5:"D", 7:"E", 9:"F#"},
        "C major": {3:"C", 5:"D", 7:"E", 8:"F", 10:"G", 0:"A", 2:"B"},
        "Eb major": {6:"Eb", 8:"F", 10:"G", 11:"Ab", 1:"Bb", 3:"C", 5:"D"},
        "F# minor": {9:"F#", 11:"G#", 0:"A", 2:"B", 4:"C#", 5:"D", 7:"E"},
        "G minor": {10:"G", 0:"A", 1:"Bb", 3:"C", 5:"D", 6:"Eb", 8:"F"}}

for i in range(num):
    freq = float(input())
    freq = freq / 440.0
    while freq >= 2.0:
        freq = freq / 2.0
    while freq < 1.0:
        freq = freq * 2.0
    freq = int(math.log(freq + 0.0001, 2) *12)
    pitches.append(freq)
ctr = 0
key = ""
for i in keys:
    legal = True
    for pitch in pitches:
        if pitch not in keys[i]:
            legal = False
    if legal:
        ctr += 1
        key = i
    if ctr > 1:
        break
        
if ctr == 1:
    print(key)
    for i in pitches:
        print(keys[key][i])
else:
    print("cannot determine key")
