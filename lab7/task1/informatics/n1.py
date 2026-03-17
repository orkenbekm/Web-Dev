n = int(input())

long_breaks = (n - 1) // 2
short_breaks = (n - 1) - long_breaks

total_minutes = n * 45 + long_breaks * 15 + short_breaks * 5

hours = 9 + total_minutes // 60
minutes = total_minutes % 60

print(hours, minutes)