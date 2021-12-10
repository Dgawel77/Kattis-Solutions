A = input()
B = input()
total = 0
for i in range(0, len(A)):
    if A[i] != B[i]:
        for j in range(i, len(A)):
            if A[j] != B[j]:
                #print(A[:i]+A[i:j+1][::-1]+A[j+1:])
                #print(B)
                if A[:i]+A[i:j+1][::-1]+A[j+1:] == B:
                    total += 1
                    dif = 1
                    while (i-dif >= 0) and (j+dif <= len(A)-1):
                        if A[i-dif] == A[j+dif] == B[i-dif] == B[j+dif]:
                            total += 1
                        else:
                            break
                        dif += 1
print(total)