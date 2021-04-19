# letter counts in numbers < 1000

import time
start_time = time.time()

total = 0

total += 900 * len("hundred")
total += 10 * len("teneleventwelvethirteenfourteen" +
                  "fifteensixteenseventeeneighteennineteen")
total += 100 * len("twentythirtyfortyfiftysixtyseventyeightyninety")
total += 190 * len("onetwothreefourfivesixseveneightnine")
total += 891 * len("and")
total += len("onethousand")

print(total) # 21124
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.075 ms
