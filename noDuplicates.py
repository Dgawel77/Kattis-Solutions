words = input().split()
prev = set()
for word in words:
    prev.add(word)
print("yes" if len(prev) == len(words) else "no")
