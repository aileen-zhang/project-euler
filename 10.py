# sum of primes below n

import time
start_time = time.time()

n = 2000000
primes = [True] * n
primes[0] = primes[1] = False
sum = 0

for i in range (0, n):
    if primes[i]:
        for c in range(i * i, n, i):
                primes[c] = False
        sum += i

print(sum) # 142913828922
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 592.792 ms
