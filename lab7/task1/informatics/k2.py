r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())

dx = abs(r1 - r2)
dy = abs(c1 - c2)

if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print("YES")
else:
    print("NO")
