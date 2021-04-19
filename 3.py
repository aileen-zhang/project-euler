# greatest prime factor of n

import time
start_time = time.time()

n = 600851475143
i = 1

while n != 1:
    if n % i == 0:
        n /= i
    i += 1

print(i - 1) # 6857
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 1.119 ms
