x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1, z2 = map(int, input().split())

distxy = ((y1 - x1)**2 - (y2 - x2)**2)**.5
print(distxy)
#distyz = 
#distxz =