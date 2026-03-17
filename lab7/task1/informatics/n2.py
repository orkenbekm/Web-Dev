a = int(input())
b = int(input())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
else:
    if (-b) % a == 0:
        print((-b) // a)
    else:
        print("NO")
