n = int(input())
a = list(map(int, input().split()))

found = False

for i in range(1, n):
    if a[i] * a[i-1] > 0:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
