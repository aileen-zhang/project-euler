# counting Sundays

import time
start_time = time.time()

leap = 0
month_lengths = [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
years = 100
sunday = []

for month in range(0, 12 * (years + 1) + 1):
    if month > 12 and (month // 12) % 4 == 0:
        leap = 1
    else:
        leap = 0
    if day % 7 == 0:
        sunday.append(True)
    else:
        sunday.append(False)
    day += month_lengths[month % 12]

sunday_count = sunday[12:].count(True)

print(sunday_count) # 171
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 2.079 ms
