def setup():
    global board, words
    wordsFound.clear()
    letters = set()
    for row in board:
        for letter in row:
            letters.add(letter)
    for word in words:
        if all(map(lambda x: x in letters, list(word))):
            stack = []
            for r in range(1, 5):
                for c in range(1, 5):
                    if board[r-1][c-1] == word[0]:
                        stack.append((r, c))
            for pos in stack:
                B = set()
                B.add(pos)
                if solve(pos, B, word):
                    break
                B.remove(pos)
    score = 0
    longestWord = "Z"
    for word in wordsFound:
        score += value(word)
        if len(word) > len(longestWord):
            longestWord = word
        elif len(word) == len(longestWord):
            if word < longestWord:
                longestWord = word
    print(f'{score} {longestWord} {len(wordsFound)}')
    return


def value(word):
    valChart = [0, 0, 0, 1, 1, 2, 3, 5, 11]
    return valChart[len(word)]


def solve(Spos, mark, word):
    global wordsFound
    if len(mark) == len(word):
        wordsFound.add(word)
        return True
    r = Spos[0]
    c = Spos[1]
    found = False
    for check in [(r+1, c), (r+1, c+1), (r+1, c-1), (r-1, c), (r-1, c+1), (r-1, c-1), (r, c+1), (r, c-1)]:
        r1 = check[0]
        c1 = check[1]
        if 0 < r1 < 5 and 0 < c1 < 5:
            if word[len(mark)] == board[r1-1][c1-1] and not (r1, c1) in mark:
                mark.add((r1, c1))
                found = solve((r1, c1), mark, word)
                mark.remove((r1, c1))
        if found:
            break
    return found


wordsFound = set()
R = int(input())
words = []
for _ in range(0, R):
    words.append(input())
input()

B = int(input())
boards = []
for _ in range(0, B-1):
    board = []
    for _ in range(0, 4):
        board.append(input())
    boards.append(board)
    input()
board = []
for _ in range(0, 4):
    board.append(input())
boards.append(board)

for x in boards:
    board = x
    setup()