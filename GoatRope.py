def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

R = list(map(int, input().split()))
corners = [(R[0], R[1]),(R[2],R[3]), (R[2],R[5]), (R[4],R[5]), (R[4],R[3])]
if R[0] > R[4]:
    if R[3] <= R[1] <= R[5]:
        print(R[0] - R[4])
    elif R[1] > R[5]:
        print(dist(corners[3], corners[0]))
    else:
        print(dist(corners[4], corners[0]))
elif R[0] < R[2]:
    if R[3] <= R[1] <= R[5]:
        print(R[2]-R[0])
    elif R[1] > R[5]:
        print(dist(corners[2], corners[0]))
    else:
        print(dist(corners[1], corners[0]))
elif R[1] < R[3]:
    print(R[3] - R[1])
elif R[1] > R[5]:
    print(R[1] - R[5])
