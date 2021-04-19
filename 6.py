# difference of sum of square and square of sum

import time
start_time = time.time()

n = 100
i = 0
sum = 0
sum_sq = 0

while i <= n:
    sum_sq += i ** 2
    sum += i
    i += 1

sq_sum = sum ** 2

print(sq_sum - sum_sq) # 25164150
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.125 ms
