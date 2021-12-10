import math
R = int(input())
freqs = set()
order = []
translate = {}
for _ in range(0, R):
    I = float(input())
    if I not in freqs:
        order.append(I)
        freqs.add(I)
# pitch = {}
# for x in range(0, 12):
#     pitch[x] = set()
pitch = {0: {"A"}, 
         1: {"A#", "Bb"}, 
         2: {"B"}, 
         3: {"C"}, 
         4: {"C#", "Db"}, 
         5: {"D"}, 
         6: {"D#", "Eb"}, 
         7: {"E"}, 
         8: {"F"},
         9: {"F#", "Gb"},
         10: {"G"},
         11: {"G#", "Ab"}}
# pitch[0].add("A")
# pitch[1].add("A#")
# pitch[1].add("Bb")
# pitch[2].add("B")
# pitch[3].add("C")
# pitch[4].add("C#")
# pitch[4].add("Db")
# pitch[5].add("D")
# pitch[6].add("D#")
# pitch[6].add("Eb")
# pitch[7].add("E")
# pitch[8].add("F")
# pitch[9].add("F#")
# pitch[9].add("Gb")
# pitch[10].add("G")
# pitch[11].add("G#")
# pitch[11].add("Ab")

posNotes = set()
keys = [("G major", {"G", "A", "B", "C", "D", "E", "F#"}),
        ("C major", {"C", "D", "E", "F", "G", "A", "B"}),
        ("Eb major", {"Eb", "F", "G", "Ab", "Bb", "C", "D"}),
        ("F# major", {"F#", "G#", "A", "B", "C#", "D", "E"}),
        ("G minor", {"G", "A", "Bb", "C", "D", "Eb", "F"}),
]
for freq in freqs:
    note = pitch[abs(round(math.log(freq / 440, 2)*12)%12)]
    posNotes = posNotes.union(set(note))
    translate[freq] = note
    #rounded = round(freq)
    #for x in range(-54, 40):
    #    if (rounded == round(440 * (2 ** (x/12)))):
    #        posNotes.append((freq, pitch[x%12]))
print(posNotes)
print(translate)
keyFound = ""
numkeys = 0
notesInKey = []
for key in keys:
    if posNotes.issubset(key[1]):
        numkeys += 1
    # if all(list(map(lambda x: x[1][0] in key[1] or x[1][-1] in key[1], posNotes))):
    #     numkeys += 1
    #     keyFound = key[0]
    #     for note in posNotes:
    #         if note[1][0] in key[1]:
    #             notesInKey.append(note[1][0])
    #             translate[note[0]] = note[1][0]
    #         elif note[1][-1] in key[1]:
    #             notesInKey.append(note[1][-1])
    #             translate[note[0]] = note[1][-1]
if numkeys != 1:
    print("cannot determine key")
else:
    print(keyFound)
    for ord in order:
        print(translate[ord])
        
