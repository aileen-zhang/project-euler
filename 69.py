# (lazy) totient maximum

import time
start_time = time.time()

n = 100
primes = [True] * n
primes[0] = primes[1] = False
product = 1

for i, p in enumerate(primes):
    if p:
        for c in range(i*i, n, i):
                primes[c] = False
        if product * i < 1000000:
            product *= i

print(product) # 510510
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.070 ms
