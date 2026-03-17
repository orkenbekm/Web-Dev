h = int(input())
a = int(input())
b = int(input())

days = (h - a + (a - b) - 1) // (a - b) + 1

print(days)