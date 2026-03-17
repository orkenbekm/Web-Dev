n = int(input())

minutes_in_day = n % 1440

hours = minutes_in_day // 60
minutes = minutes_in_day % 60

print(hours, minutes)
