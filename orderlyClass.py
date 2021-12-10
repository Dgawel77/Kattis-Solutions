A = input()
B = input()
total = 0
i = 0
while A[i] == B[i]:
    i += 1
j = len(A)-1
while A[j] == B[j]:
    j -= 1
if A[i:j+1][::-1] == B[i:j+1]:
    total += 1
    dif = 1
    while (i-dif >= 0) and (j+dif <= len(A)-1):
        if A[i-dif] == A[j+dif] == B[i-dif] == B[j+dif]:
            total += 1
        else:
            break
        dif += 1
print(total)