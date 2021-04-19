# find nth prime

import math
import time
start_time = time.time()

n = 10001
primes = [2]
i = 3

while len(primes) < n:
    for prime in primes:
        if i % prime == 0:
            break
        elif prime > math.sqrt(i):
            primes.append(i)
            break
    i += 2

print(primes[-1]) # 104743
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 223.834 ms
