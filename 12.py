# highly divisible triangular number with more than f factors

import numpy as np
import time
start_time = time.time()

f = 500
primes = [2]
i = 3

while len(primes) < f:
    for prime in primes:
        if i % prime == 0:
            break
        elif prime > np.sqrt(i):
            primes.append(i)
            break
    i += 2

def triangle(n):
    return n * (n + 1) / 2

def factor_count(n):
    factors = {}
    sum = 1
    for prime in primes:
        if prime <= np.sqrt(n):
            factors[prime] = 0
            while n % prime == 0:
                n /= prime
                factors[prime] += 1
        else:
            break
    if n != 1:
        factors[n] = 1
    for f in factors:
        sum *= (factors[f] + 1)
    return sum

n = 1
while factor_count(triangle(n)) < f:
    n += 1

print(int(triangle(n))) # 76576500
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 780.738 ms
