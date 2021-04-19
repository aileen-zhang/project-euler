# sum of multiples of 3 or 5

import time
start_time = time.time()

n = 1000
i = 0
sum = 0
while i < n:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1

print(sum) # 233168
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.423 ms
